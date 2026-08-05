import joblib
import pandas as pd

from ml.config import (
    STRESS_RF_MODEL_PATH,
    STRESS_LABEL_ENCODER_PATH
)

'''
#Load Model
def load_model():

    model = joblib.load(
        STRESS_RF_MODEL_PATH
    )

    return model


#Load Label Encoder
def load_label_encoder():

    label_encoder = joblib.load(
        STRESS_LABEL_ENCODER_PATH
    )

    return label_encoder
'''

# Load once
model = joblib.load(STRESS_RF_MODEL_PATH)
label_encoder = joblib.load(STRESS_LABEL_ENCODER_PATH)


def predict_stress(
    soil_moisture,
    solar_radiation,
    air_temperature,
    relative_humidity,
    vpd
):

    input_data = pd.DataFrame(
        [{
            "Soil_Moisture": soil_moisture,
            "Solar_Radiation": solar_radiation,
            "Air_Temperature": air_temperature,
            "Relative_Humidity": relative_humidity,
            "VPD": vpd
        }]
    )

    prediction = model.predict(input_data)

    stress = label_encoder.inverse_transform(
        prediction
    )[0]

    return stress

#Main Function
def main():

    stress = predict_stress(
        soil_moisture=68.5,
        solar_radiation=52000,
        air_temperature=30.4,
        relative_humidity=62.5,
        vpd=1.75
    )

    print("\nStress Prediction\n")
    print(f"Predicted Stress Level : {stress}")


if __name__ == "__main__":
    main()