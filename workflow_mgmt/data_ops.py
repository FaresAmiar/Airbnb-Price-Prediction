import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

def load_dataset(file_path: str):
    """Load the dataset from a given file path."""
    return pd.read_csv(file_path)

def preprocess_dataset(data: pd.DataFrame):
    """Preprocess the dataset by handling missing values and transformations."""
    data['reviews_per_month'] = data['reviews_per_month'].fillna(0)

    data = data[(data['price'] >= 10) & (data['price'] <= 1000)]

    return data

def split_dataset(data: pd.DataFrame, test_size=0.2, random_state=42):
    """Split the data into training and test sets."""
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
    return train_data, test_data

def transform_dataset(train: pd.DataFrame, test: pd.DataFrame):
    """Transform the dataset, encode categorical variables and split features from target."""
    features = ['latitude', 'longitude', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
                'calculated_host_listings_count', 'availability_365', 'room_type']
    target = 'price'

    y_train = train[target].values
    y_test = test[target].values

    dv = DictVectorizer(sparse=False)
    train_dicts = train[features].to_dict(orient='records')
    X_train = dv.fit_transform(train_dicts)

    test_dicts = test[features].to_dict(orient='records')
    X_test = dv.transform(test_dicts)

    return X_train, y_train, X_test, y_test, dv
