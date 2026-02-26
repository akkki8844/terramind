import sys
from core.predictor import predict_impact
from utils.suggestions import generate_suggestions


VALID_TRANSPORT = ["car", "bus", "bike", "train"]
VALID_LEVELS = ["low", "medium", "high"]
VALID_YES_NO = ["yes", "no"]


def get_input(prompt, valid_options):
    while True:
        value = input(prompt).strip().lower()
        if value in valid_options:
            return value
        else:
            print(f"Invalid input. Choose from: {', '.join(valid_options)}\n")


def display_banner():
    print("\n" + "=" * 50)
    print("🌍 TerraMind - Climate Impact AI")
    print("=" * 50)
    print("Analyze your daily habits and discover your")
    print("environmental impact level.\n")


def collect_user_data():
    print("Please enter your daily habits:\n")

    transport = get_input(
        "Transport (car/bus/bike/train): ",
        VALID_TRANSPORT
    )

    electricity = get_input(
        "Electricity usage (low/medium/high): ",
        VALID_LEVELS
    )

    recycling = get_input(
        "Recycling (yes/no): ",
        VALID_YES_NO
    )

    meat = get_input(
        "Meat consumption (low/medium/high): ",
        VALID_LEVELS
    )

    water = get_input(
        "Water usage (low/medium/high): ",
        VALID_LEVELS
    )

    return {
        "transport": transport,
        "electricity": electricity,
        "recycling": recycling,
        "meat_consumption": meat,
        "water_usage": water
    }


def display_results(prediction):
    print("\n" + "-" * 50)
    print(f"Predicted Environmental Impact: {prediction.upper()}")
    print("-" * 50)

    suggestions = generate_suggestions(prediction)

    print("\nRecommended Climate Solutions:")
    for s in suggestions:
        print(f"- {s}")

    print("\nThank you for using TerraMind.")
    print("=" * 50 + "\n")


def run():
    display_banner()
    user_data = collect_user_data()

    try:
        prediction = predict_impact(user_data)
        display_results(prediction)
    except Exception as e:
        print("An error occurred while analyzing data.")
        print(str(e))
        sys.exit(1)


if __name__ == "__main__":
    run()