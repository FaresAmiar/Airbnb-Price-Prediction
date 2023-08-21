import pandas as pd
from evidently.dashboard import Dashboard
from evidently.tabs import DriftTab

class EvidentlyReport:
    def __init__(self, train_data, test_data, target, numerical_features=None, categorical_features=None):
        self.train_data = train_data
        self.test_data = test_data
        self.target = target
        self.numerical_features = numerical_features or []
        self.categorical_features = categorical_features or []

    def get_column_mapping(self):
        column_mapping = {
            'target': self.target,
            'numerical_features': self.numerical_features,
            'categorical_features': self.categorical_features
        }
        return column_mapping

    def generate_report(self, save_path='report.html'):
        column_mapping = self.get_column_mapping()
        drift_dashboard = Dashboard(tabs=[DriftTab])
        drift_dashboard.calculate(self.train_data, self.test_data, column_mapping=column_mapping)
        drift_dashboard.save(save_path)
