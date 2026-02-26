import pandas as pd
import yaml
import os
from sklearn.preprocessing import OneHotEncoder
import joblib


def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


def load_raw_data(config):
    path = config["paths"]["raw_data"]

    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at {path}")

    return pd.read_csv(path)


def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Drop rows with missing values
    df = df.dropna()

    return df


def save_cleaned_data(df, config):
    cleaned_path = config["paths"]["cleaned_data"]
    df.to_csv(cleaned_path, index=False)


def encode_features(df, config):
    feature_columns = config["features"]["categorical"]
    target_column = config["features"]["target"]

    X = df[feature_columns]
    y = df[target_column]

    encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    X_encoded = encoder.fit_transform(X)

    return X_encoded, y, encoder


def preprocess_pipeline():
    config = load_config()

    df = load_raw_data(config)
    df = clean_data(df)
    save_cleaned_data(df, config)

    X_encoded, y, encoder = encode_features(df, config)

    return X_encoded, y, encoder