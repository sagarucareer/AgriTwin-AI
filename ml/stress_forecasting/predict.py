import numpy as np
import joblib
from tensorflow.keras.models import load_model
from ml.config import (
    STRESS_DATASET_PATH,
    STRESS_LSTM_MODEL_PATH,
    STRESS_RF_MODEL_PATH,
    SCALER_PATH,
    LABEL_ENCODER_PATH
)

#Load Models
'''
def load_models():

    lstm_model = load_model(STRESS_LSTM_MODEL_PATH)
    rf_model = joblib.load(STRESS_RF_MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    return (lstm_model, rf_model, scaler)
'''

# Load Models Once
lstm_model = load_model(STRESS_LSTM_MODEL_PATH)
rf_model = joblib.load(STRESS_RF_MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
label_encoder = joblib.load(LABEL_ENCODER_PATH)

#Load Latest Readings
def load_latest_readings():

    data = np.loadtxt(
        STRESS_DATASET_PATH,
        delimiter=",",
        skiprows=1,
        usecols=(1, 2, 3, 4, 5)
    )

    latest_sequence = data[-24:]

    return latest_sequence

#Predict Future Sensor Values
def forecast_sensor_values(latest_sequence):

    scaled_sequence = scaler.transform(latest_sequence)
    lstm_input = np.expand_dims(scaled_sequence, axis=0)

    prediction = lstm_model.predict(lstm_input, verbose=0)
    prediction = np.clip(prediction, 0, 1)
    predicted_values = scaler.inverse_transform(prediction)

    return predicted_values[0]

#Predict Future Stress
def predict_future_stress(predicted_values):

    future_stress = rf_model.predict(predicted_values.reshape(1, -1))

    future_stress = label_encoder.inverse_transform(future_stress)

    return future_stress[0]

#Display Results
def display_results(predicted_values, future_stress):

    print("\nForecasted Sensor Values\n")

    print(f"Soil Moisture      : {predicted_values[0]:.2f} %")
    print(f"Solar Radiation    : {predicted_values[1]:.2f} lux")
    print(f"Air Temperature    : {predicted_values[2]:.2f} °C")
    print(f"Relative Humidity  : {predicted_values[3]:.2f} %")
    print(f"VPD                : {predicted_values[4]:.2f} kPa")

    print("\nFuture Stress Prediction\n")

    print(f"Predicted Stress Level : {future_stress}")

#Function imported in flask
def forecast_stress(latest_sequence):

    predicted_values = forecast_sensor_values(
        latest_sequence
    )

    future_stress = predict_future_stress(
        predicted_values
    )

    return predicted_values, future_stress

#Main Function
#Main Function
def main():

    latest_sequence = load_latest_readings()

    predicted_values, future_stress = forecast_stress(
        latest_sequence
    )

    display_results(
        predicted_values,
        future_stress
    )


if __name__ == "__main__":

    main()