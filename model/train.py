"""
TerraMind Model Training Script
Trains ML model and saves artifacts.
"""

import joblib
import yaml
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from core.preprocessing import preprocess_pipeline


def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


def build_model(config):
    model_type = config["model"]["type"]
    random_state = config["model"]["random_state"]

    if model_type == "decision_tree":
        return DecisionTreeClassifier(
            max_depth=config["model"]["max_depth"],
            random_state=random_state
        )

    elif model_type == "random_forest":
        return RandomForestClassifier(
            n_estimators=100,
            random_state=random_state
        )

    else:
        raise ValueError("Unsupported model type in config.yaml")


def train():
    config = load_config()

    print("\nLoading and preprocessing dataset...")
    X_encoded, y, encoder = preprocess_pipeline()

    test_size = config["training"]["test_size"]
    random_state = config["model"]["random_state"]

    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y if config["training"]["stratify"] else None
    )

    print("Building model...")
    model = build_model(config)

    print("Training model...")
    model.fit(X_train, y_train)

    print("Evaluating training performance...")
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Validation Accuracy: {accuracy:.4f}")

    # Save model
    model_path = config["paths"]["model_path"]
    encoder_path = config["paths"]["encoder_path"]

    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    joblib.dump(model, model_path)
    joblib.dump(encoder, encoder_path)

    print("\nModel and encoder saved successfully.")
    print("Training complete.\n")


if __name__ == "__main__":
    train()