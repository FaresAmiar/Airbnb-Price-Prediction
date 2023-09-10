from itertools import product
import pandas as pd
from prefect import task, flow
from data_ops import load_dataset, preprocess_dataset, split_dataset, transform_dataset
from model_ops import train_model, evaluate_model
from ModelWrapper import ModelWrapper

from evidently.metrics import DatasetDriftMetric
from evidently_monitoring import calculate_metrics_with_evidently


import mlflow
import mlflow.pyfunc
import joblib
import os
import json



with open('config.json', 'r') as file:
    config = json.load(file)

deployment_mode = config["deployment_mode"]
mlflow_settings = config['mlflow'][deployment_mode]

model_info = config['model']
best_run_id = None

backend_url = mlflow_settings["backend_uri"]
EXPERIMENT_NAME = mlflow_settings['experiment_name']


@task
def load_task():
    return load_dataset("./data/AB_NYC_2019.csv")

@task
def preprocess_task(data):
    return preprocess_dataset(data)

@task
def split_task(data):
    return split_dataset(data)

@task
def transform_task(train, test):
    X_train, y_train, X_test, y_test, dv = transform_dataset(train, test)
    joblib.dump(dv, "dict_vectorizer.pkl")
    return X_train, y_train, X_test, y_test

@task
def train_and_evaluate_task(X_train, y_train, X_test, y_test, model_module, model_name,hyper_params):
    model = train_model(X_train, y_train, model_module, model_name, hyper_params)
    metric_value, predictions = evaluate_model(model, X_test, y_test, model_info)
    wrapped_model = ModelWrapper(model)
    mlflow.log_artifact("dict_vectorizer.pkl")
    mlflow.pyfunc.log_model("model", python_model=wrapped_model)
    return metric_value, wrapped_model, predictions

@task
def monitor_metrics(X_test, y_test, predictions):
    report = calculate_metrics_with_evidently(X_test, y_test, predictions)

    metric_threshold = config['model']['metric']['threshold']
    metric_val = report.get_metric_value(DatasetDriftMetric())

    if metric_val > metric_threshold:
        print(f"ALERT: Metric exceeded the threshold! Current Value: {metric_val}")
        return True
    return False


@flow
def main_flow_airbnb():
    mlflow.set_tracking_uri(backend_url)
    mlflow.set_experiment(EXPERIMENT_NAME)
    if config['model']['grid_search']['enable']:
        param_grid = config['model']['grid_search']['parameters']
        hyperparameters_list = [dict(zip(param_grid.keys(), values)) for values in product(*param_grid.values())]
    elif config['model']['parameters'] is not None:
        hyperparameters = config['model']['parameters']
    else:
        hyperparameters_list = [{}]

    for hyperparameters in hyperparameters_list:
        mlflow.start_run()
        data = load_task()
        preprocessed_data = preprocess_task(data)
        train, test = split_task(preprocessed_data)
        X_train, y_train, X_test, y_test = transform_task(train, test)
        metric_value, model, predictions = train_and_evaluate_task(X_train, y_train, X_test, y_test, model_info["module"], model_info["name"], hyperparameters)

        # retrain_needed = monitor_metrics(X_test, y_test, predictions)

        # if retrain_needed:
        #     pass

        mlflow.end_run()

if __name__ == "__main__":
    main_flow_airbnb()
