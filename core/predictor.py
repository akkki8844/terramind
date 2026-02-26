import joblib
import yaml
import os
import pandas as pd


# Load configuration
def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


# Load trained model and encoder
def load_artifacts(config):
    model_path = config["paths"]["model_path"]
    encoder_path = config["paths"]["encoder_path"]

    if not os.path.exists(model_path):
        raise FileNotFoundError("Trained model not found. Run training first.")

    if not os.path.exists(encoder_path):
        raise FileNotFoundError("Encoder not found. Run training first.")

    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)

    return model, encoder


# Prepare input data for prediction
def preprocess_input(user_data, encoder, config):
    feature_columns = config["features"]["categorical"]

    df = pd.DataFrame([user_data])
    df = df[feature_columns]  # Ensure correct order

    encoded = encoder.transform(df)

    return encoded


# Main prediction function
def predict_impact(user_data):
    config = load_config()
    model, encoder = load_artifacts(config)

    processed_input = preprocess_input(user_data, encoder, config)

    prediction = model.predict(processed_input)[0]

    return prediction