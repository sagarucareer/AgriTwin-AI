import sys
import os
import numpy as np
from datetime import datetime, timedelta

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
)

from ml.stress_forecasting.predict import forecast_stress

from database.crud import (
    get_latest_sensor_sequence,
    save_stress_forecast,
    save_stress_prediction,
    save_alert
)


def predict_forecast(plant_id):

    sequence = get_latest_sensor_sequence(plant_id)

    latest_sequence = np.array([
        [
            row["soil_moisture"],
            row["solar_radiation"],
            row["air_temperature"],
            row["relative_humidity"],
            row["vpd"]
        ]
        for row in sequence
    ])

    predicted_values, future_stress = forecast_stress(
        latest_sequence
    )

    forecast_time = datetime.now() + timedelta(hours=1)

    save_stress_forecast(
        plant_id=plant_id,
        forecast_time=forecast_time,
        predicted_soil_moisture=float(predicted_values[0]),
        predicted_solar_radiation=float(predicted_values[1]),
        predicted_air_temperature=float(predicted_values[2]),
        predicted_relative_humidity=float(predicted_values[3]),
        predicted_vpd=float(predicted_values[4])
    )

    save_stress_prediction(
        plant_id=plant_id,
        prediction_type="Forecast",
        stress_level=future_stress,
        confidence=None
    )

    if future_stress == "High":
        save_alert(
            plant_id=plant_id,
            alert_type="Forecast",
            message="High stress predicted in the next hour."
        )

    return {

        "forecast_time": forecast_time,

        "predicted_soil_moisture": float(predicted_values[0]),

        "predicted_solar_radiation": float(predicted_values[1]),

        "predicted_air_temperature": float(predicted_values[2]),

        "predicted_relative_humidity": float(predicted_values[3]),

        "predicted_vpd": float(predicted_values[4]),

        "future_stress": future_stress

    }