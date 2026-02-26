"""
TerraMind Unit Tests
Basic functional testing for model pipeline.
"""

import unittest
import os
import joblib
import yaml
from core.predictor import predict_impact


class TestTerraMindModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load config
        with open("config/config.yaml", "r") as file:
            cls.config = yaml.safe_load(file)

        cls.model_path = cls.config["paths"]["model_path"]
        cls.encoder_path = cls.config["paths"]["encoder_path"]

    def test_model_files_exist(self):
        """Check if trained model files exist"""
        self.assertTrue(os.path.exists(self.model_path),
                        "Model file not found. Run training first.")
        self.assertTrue(os.path.exists(self.encoder_path),
                        "Encoder file not found. Run training first.")

    def test_prediction_output(self):
        """Check if prediction returns valid label"""

        sample_input = {
            "transport": "car",
            "electricity": "high",
            "recycling": "no",
            "meat_consumption": "high",
            "water_usage": "high"
        }

        prediction = predict_impact(sample_input)

        self.assertIn(prediction, ["low", "medium", "high"],
                      "Prediction output is invalid.")

    def test_model_loadable(self):
        """Ensure model can be loaded without error"""
        model = joblib.load(self.model_path)
        self.assertIsNotNone(model)


if __name__ == "__main__":
    unittest.main()