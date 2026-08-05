import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
)

from ml.stress_prediction.predict import predict_stress

from database.crud import (
    save_sensor_reading,
    save_stress_prediction,
    save_alert
)


def detect_stress(
    plant_id,
    soil_moisture,
    solar_radiation,
    air_temperature,
    relative_humidity,
    vpd
):

    save_sensor_reading(
        plant_id=plant_id,
        soil_moisture=soil_moisture,
        solar_radiation=solar_radiation,
        air_temperature=air_temperature,
        relative_humidity=relative_humidity,
        vpd=vpd
    )

    stress = predict_stress(
        soil_moisture=soil_moisture,
        solar_radiation=solar_radiation,
        air_temperature=air_temperature,
        relative_humidity=relative_humidity,
        vpd=vpd
    )

    save_stress_prediction(
        plant_id=plant_id,
        prediction_type="Current",
        stress_level=stress,
        confidence=None
    )

    if stress == "High":
        save_alert(
            plant_id=plant_id,
            alert_type="Stress",
            message="High stress detected."
        )

    return {
        "stress_level": stress
    }