import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
)

from database.crud import (
    get_latest_sensor_reading,
    get_latest_disease_prediction,
    get_latest_stress_prediction,
    get_latest_stress_forecast,
    get_latest_irrigation,
    get_latest_alert
)


def get_dashboard_data(plant_id):

    return {

        "sensor": get_latest_sensor_reading(
            plant_id
        ),

        "disease": get_latest_disease_prediction(
            plant_id
        ),

        "stress": get_latest_stress_prediction(
            plant_id
        ),

        "forecast": get_latest_stress_forecast(
            plant_id
        ),

        "irrigation": get_latest_irrigation(
            plant_id
        ),

        "alert": get_latest_alert(
            plant_id
        )

    }