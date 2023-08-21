import pandas as pd
from evidently import ColumnMapping
from evidently.report import Report


from data_ops import load_dataset, preprocess_dataset
import mlflow

def load_data(file_path):
    return load_dataset(file_path)

def load_model(run_id):
    model = mlflow.pyfunc.load_model(f"runs:/{run_id}/model")
    return model

# def calculate_metrics(reference_data_path, current_data_path, run_id):
#     reference_data = load_data(reference_data_path)
#     current_data = load_data(current_data_path)

#     model = load_model(run_id)

#     X_current, _ = preprocess_dataset(current_data)
#     predictions = model.predict(X_current)

#     column_mapping = {
#         'numerical_features': ["latitude", "longitude", "minimum_nights", "number_of_reviews", "reviews_per_month", "calculated_host_listings_count", "availability_365"],
#         'categorical_features': ["neighbourhood_group", "room_type"],
#         'target': 'price'
#     }

#     drift_dashboard = Dashboard(tabs=[DataDriftTab])
#     drift_dashboard.calculate(reference_data, current_data, column_mapping=column_mapping)
#     drift_dashboard.save('drift_report.html')

def calculate_metrics_with_evidently(X_test, y_test, predictions):
    column_mapping = ColumnMapping(
        target='price',
        numerical_features=["latitude", "longitude", "minimum_nights", "number_of_reviews", "reviews_per_month", "calculated_host_listings_count", "availability_365"]
    )

    X_test_df = pd.DataFrame(X_test)
    y_test_series = pd.Series(y_test, name='price_actual', index=X_test_df.index)
    predictions_series = pd.Series(predictions, name='price_predicted', index=X_test_df.index)

    current_data = pd.concat([X_test_df, y_test_series, predictions_series], axis=1)

    report = Report(
        type_name='data_drift',
        column_mapping=column_mapping
    )
    report.run(pd.concat([X_test_df, y_test], axis=1), current_data)

    return report


# if __name__ == "__main__":
#     REFERENCE_DATA_PATH = "./data/AB_NYC_2019.csv"
#     CURRENT_DATA_PATH = "./data/AB_NYC_2019.csv"
#     RUN_ID = ""

#     calculate_metrics(REFERENCE_DATA_PATH, CURRENT_DATA_PATH, RUN_ID)
