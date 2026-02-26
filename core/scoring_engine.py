"""
TerraMind Scoring Engine
Adds weighted environmental scoring logic
on top of ML prediction for transparency.
"""

# Impact mapping
IMPACT_SCORE_MAP = {
    "low": 1,
    "medium": 2,
    "high": 3
}


def compute_weighted_score(user_data):
    """
    Assign weighted environmental score based on habits.
    Higher score = higher environmental impact.
    """

    score = 0

    # Transport weight
    transport_weights = {
        "bike": 1,
        "train": 2,
        "bus": 2,
        "car": 3
    }

    # Electricity weight
    level_weights = {
        "low": 1,
        "medium": 2,
        "high": 3
    }

    # Recycling weight (reverse impact)
    recycling_weights = {
        "yes": 1,
        "no": 3
    }

    score += transport_weights.get(user_data["transport"], 2)
    score += level_weights.get(user_data["electricity"], 2)
    score += recycling_weights.get(user_data["recycling"], 2)
    score += level_weights.get(user_data["meat_consumption"], 2)
    score += level_weights.get(user_data["water_usage"], 2)

    return score


def interpret_score(score):
    """
    Convert numerical score to impact label.
    """

    if score <= 6:
        return "low"
    elif 7 <= score <= 10:
        return "medium"
    else:
        return "high"


def final_decision(ml_prediction, user_data):
    """
    Combine ML prediction with weighted scoring.
    If there's disagreement, weighted score has priority.
    """

    weighted_score = compute_weighted_score(user_data)
    weighted_label = interpret_score(weighted_score)

    # If ML and weighted disagree, prioritize weighted logic
    if weighted_label != ml_prediction:
        return weighted_label

    return ml_prediction