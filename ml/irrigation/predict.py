from ml.irrigation.irrigation_pipeline import (
    irrigation_decision
)


def recommend_irrigation(
    current_stress,
    future_stress,
    current_soil_moisture,
    future_soil_moisture,
    current_vpd,
    future_vpd
):

    return irrigation_decision(
        current_stress,
        future_stress,
        current_soil_moisture,
        future_soil_moisture,
        current_vpd,
        future_vpd
    )


def main():

    decision = recommend_irrigation(
        current_stress="Medium",
        future_stress="High",
        current_soil_moisture=52.8,
        future_soil_moisture=41.3,
        current_vpd=1.85,
        future_vpd=2.46
    )

    print("\nIrrigation Decision\n")

    print(
        f"Irrigation Required : "
        f"{'YES' if decision['irrigation_required'] else 'NO'}"
    )

    print(
        f"Pump Duration       : "
        f"{decision['pump_duration']} seconds"
    )

    print(
        f"Reason              : "
        f"{decision['reason']}"
    )


if __name__ == "__main__":
    main()