import mlflow

import importlib

def train_model(X_train, y_train, model_module, model_name, hyper_params):
    model_module = importlib.import_module(model_module)
    model_class = getattr(model_module, model_name)

    model = model_class(**hyper_params)

    for param_name, param_value in hyper_params.items():
        mlflow.log_param(param_name, param_value)

    model.fit(X_train, y_train)
    return model



def evaluate_model(model, X, y, model_info):
    metric_module = importlib.import_module(model_info['metric']['module'])
    metric_func = getattr(metric_module, model_info['metric']['func'])
    y_pred = model.predict(X)
    metric_name, metric_value = model_info['metric']['func'], metric_func(y, y_pred)
    mlflow.log_metric(metric_name, metric_value)
    return metric_value, y_pred
