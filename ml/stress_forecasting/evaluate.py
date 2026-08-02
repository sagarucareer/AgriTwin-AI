import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error
)
from ml.config import (
    STRESS_LSTM_MODEL_PATH
)
from ml.stress_forecasting.preprocess import (
    load_dataset,
    preprocess_data,
    create_sequences,
    split_dataset
)

#Load Model
def load_lstm_model():

    model = load_model(
        STRESS_LSTM_MODEL_PATH
    )

    return model


#Evaluate Model
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(
        X_test,
        verbose=0
    )
    mse = mean_squared_error(
        y_test,
        predictions
    )
    mae = mean_absolute_error(
        y_test,
        predictions
    )
    rmse = np.sqrt(mse)

    print("\nLSTM Model Evaluation\n")

    print(f"MSE  : {mse:.6f}")
    print(f"MAE  : {mae:.6f}")
    print(f"RMSE : {rmse:.6f}")

    return predictions

#Display Sample Predictions
def display_predictions(y_test, predictions):

    print("\nSample Predictions\n")

    feature_names = [
        "Soil Moisture",
        "Solar Radiation",
        "Air Temperature",
        "Relative Humidity",
        "VPD"
    ]

    for sample in range(5):
        print(f"\nSample {sample + 1}")

        for feature in range(len(feature_names)):
            print(
                f"{feature_names[feature]:20}"
                f"Actual : {y_test[sample][feature]:.4f}"
                f"    "
                f"Predicted : {predictions[sample][feature]:.4f}"
            )

#Main Function
def main():

    df = load_dataset()

    scaled_data, _ = preprocess_data(df)

    X, y = create_sequences(scaled_data)
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    model = load_lstm_model()
    predictions = evaluate_model(model, X_test, y_test)
    display_predictions(y_test, predictions)


if __name__ == "__main__":

    main()
