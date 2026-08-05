import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
)

from ml.irrigation.predict import (
    recommend_irrigation
)

from database.crud import (
    save_irrigation_recommendation,
    save_alert
)


def get_irrigation_recommendation(

    plant_id,

    current_stress,
    future_stress,

    current_soil_moisture,
    future_soil_moisture,

    current_vpd,
    future_vpd

):

    decision = recommend_irrigation(

        current_stress=current_stress,
        future_stress=future_stress,

        current_soil_moisture=current_soil_moisture,
        future_soil_moisture=future_soil_moisture,

        current_vpd=current_vpd,
        future_vpd=future_vpd

    )

    save_irrigation_recommendation(

        plant_id=plant_id,
        pump_duration_seconds=decision["pump_duration"],
        reason=decision["reason"]

    )

    if decision["irrigation_required"]:
        save_alert(
            plant_id=plant_id,
            alert_type="Irrigation",
            message=(
                f"Irrigation recommended for "
                f"{decision['pump_duration']} seconds."
            )
        )

    return decision