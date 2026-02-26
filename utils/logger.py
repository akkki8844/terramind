"""
TerraMind Logger Utility
Centralized logging configuration.
"""

import logging
import yaml
import os


def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


def setup_logger(name="terramind"):
    config = load_config()
    log_level = config["logging"]["level"].upper()

    level = getattr(logging, log_level, logging.INFO)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        if config["logging"]["save_logs"]:
            os.makedirs("logs", exist_ok=True)
            file_handler = logging.FileHandler("logs/terramind.log")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger