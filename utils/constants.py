"""
TerraMind Constants
Centralized definitions for valid inputs and system labels.
"""

# Valid user inputs
VALID_TRANSPORT = ["car", "bus", "bike", "train"]
VALID_LEVELS = ["low", "medium", "high"]
VALID_YES_NO = ["yes", "no"]

# Impact Labels
IMPACT_LABELS = ["low", "medium", "high"]

# Transport Environmental Weights
TRANSPORT_WEIGHTS = {
    "bike": 1,
    "train": 2,
    "bus": 2,
    "car": 3
}

# Level Weights (electricity, meat, water)
LEVEL_WEIGHTS = {
    "low": 1,
    "medium": 2,
    "high": 3
}

# Recycling Weights (reverse impact logic)
RECYCLING_WEIGHTS = {
    "yes": 1,
    "no": 3
}

# Terminal Styling (optional future upgrade)
BANNER_LINE = "=" * 50
SECTION_LINE = "-" * 50

APP_NAME = "TerraMind"
APP_VERSION = "1.0"