"""
TerraMind Model Evaluation Script
Evaluates trained model performance.
"""

import joblib
import yaml
import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split


def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


def load_artifacts(config):
    model = joblib.load(config["paths"]["model_path"])
    encoder = joblib.load(config["paths"]["encoder_path"])
    return model, encoder


def load_dataset(config):
    path = config["paths"]["cleaned_data"]
    if not os.path.exists(path):
        path = config["paths"]["raw_data"]
    return pd.read_csv(path)


def prepare_data(df, encoder, config):
    feature_columns = config["features"]["categorical"]
    target_column = config["features"]["target"]

    X = df[feature_columns]
    y = df[target_column]

    X_encoded = encoder.transform(X)

    return X_encoded, y


def evaluate():
    config = load_config()
    model, encoder = load_artifacts(config)
    df = load_dataset(config)

    X_encoded, y = prepare_data(df, encoder, config)

    test_size = config["training"]["test_size"]
    random_state = config["model"]["random_state"]

    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=test_size, random_state=random_state
    )

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average="weighted", zero_division=0)
    recall = recall_score(y_test, predictions, average="weighted", zero_division=0)
    f1 = f1_score(y_test, predictions, average="weighted", zero_division=0)

    report = f"""
TerraMind Model Evaluation Report
----------------------------------
Accuracy:  {accuracy:.4f}
Precision: {precision:.4f}
Recall:    {recall:.4f}
F1 Score:  {f1:.4f}
"""

    print(report)

    if config["evaluation"]["save_report"]:
        with open(config["paths"]["evaluation_report"], "w") as f:
            f.write(report)


if __name__ == "__main__":
    evaluate()