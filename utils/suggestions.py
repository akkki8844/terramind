"""
TerraMind Suggestions Engine
Generates personalized sustainability recommendations.
"""

from utils.constants import (
    IMPACT_LABELS
)


BASE_SUGGESTIONS = {
    "low": [
        "Maintain your sustainable habits.",
        "Encourage others to adopt eco-friendly practices.",
        "Consider supporting renewable energy initiatives."
    ],
    "medium": [
        "Reduce electricity consumption where possible.",
        "Increase recycling frequency.",
        "Reduce red meat consumption to lower carbon footprint."
    ],
    "high": [
        "Switch to public transport, biking, or carpooling.",
        "Lower electricity usage and switch to energy-efficient appliances.",
        "Reduce meat consumption significantly.",
        "Conserve water by shortening showers and fixing leaks."
    ]
}


def habit_specific_suggestions(user_data):
    suggestions = []

    if user_data.get("transport") == "car":
        suggestions.append("Consider replacing car trips with public transport or biking.")

    if user_data.get("electricity") == "high":
        suggestions.append("Turn off unused appliances and consider LED lighting.")

    if user_data.get("recycling") == "no":
        suggestions.append("Start recycling plastic, paper, and metal regularly.")

    if user_data.get("meat_consumption") == "high":
        suggestions.append("Try plant-based meals several times a week.")

    if user_data.get("water_usage") == "high":
        suggestions.append("Install low-flow fixtures to reduce water consumption.")

    return suggestions


def generate_suggestions(prediction, user_data=None):
    if prediction not in IMPACT_LABELS:
        return ["Unable to generate suggestions due to invalid prediction."]

    suggestions = list(BASE_SUGGESTIONS[prediction])

    if user_data:
        suggestions.extend(habit_specific_suggestions(user_data))

    # Remove duplicates while preserving order
    seen = set()
    final_list = []
    for s in suggestions:
        if s not in seen:
            final_list.append(s)
            seen.add(s)

    return final_list