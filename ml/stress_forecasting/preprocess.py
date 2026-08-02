import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from ml.config import (
    STRESS_DATASET_PATH,
    SCALER_PATH,
    SEQUENCE_LENGTH,
    TEST_SIZE,
    RANDOM_SEED
)

#Load Dataset
def load_dataset():

    df = pd.read_csv(
        STRESS_DATASET_PATH
    )

    return df


#Data Preprocessing
def preprocess_data(df):

    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"]
    )
    df = df.sort_values(
        by="Timestamp"
    )

    features = [
        "Soil_Moisture",
        "Solar_Radiation",
        "Air_Temperature",
        "Relative_Humidity",
        "VPD"
    ]

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(
        df[features]
    )

    return scaled_data, scaler

#Create Sequences
def create_sequences(data):

    X = []
    y = []

    for i in range(len(data) - SEQUENCE_LENGTH):

        X.append(
            data[i : i + SEQUENCE_LENGTH]
        )

        y.append(
            data[i + SEQUENCE_LENGTH]
        )

    return (
        np.array(X),
        np.array(y)
    )


#Train Test Split
def split_dataset(X, y):

    split_index = int(
        len(X) * (1 - TEST_SIZE)
    )

    X_train = X[:split_index]
    X_test = X[split_index:]

    y_train = y[:split_index]
    y_test = y[split_index:]

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )


#Save Scaler
def save_scaler(scaler):

    joblib.dump(
        scaler,
        SCALER_PATH
    )

    print("\nScaler Saved Successfully!")


#Main Function
def main():

    df = load_dataset()
    scaled_data, scaler = preprocess_data(df)

    X, y = create_sequences(
        scaled_data
    )
    X_train, X_test, y_train, y_test = split_dataset(
        X,
        y
    )

    save_scaler(scaler)

    print("\nPreprocessing Completed Successfully!\n")

    print(f"Sequence Length : {SEQUENCE_LENGTH}")

    print(f"\nTraining Samples : {len(X_train)}")
    print(f"Testing Samples  : {len(X_test)}")

    print(f"\nInput Shape : {X_train.shape}")
    print(f"Output Shape : {y_train.shape}")


if __name__ == "__main__":
    main()