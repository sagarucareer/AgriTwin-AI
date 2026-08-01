import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from ml.config import (
    STRESS_DATASET_PATH,
    STRESS_LABEL_ENCODER_PATH,
    TEST_SIZE,
    RANDOM_SEED
)


#Load Dataset
def load_dataset():

    df = pd.read_csv(STRESS_DATASET_PATH)

    return df


#Dataset Inspection
def inspect_dataset(df):

    print("\nDataset Information\n")

    print(f"Shape : {df.shape}\n")

    print("Data Types\n")
    print(df.dtypes)

    print("\nMissing Values\n")
    print(df.isnull().sum())

    print("\nDuplicate Rows :", df.duplicated().sum())

    print("\nStress Distribution\n")
    print(df["Stress"].value_counts())


#Data Preprocessing
def preprocess_data(df):

    columns_to_drop = ["Timestamp"]

    df = df.drop(columns=columns_to_drop)
    label_encoder = LabelEncoder()
    df["Stress"] = label_encoder.fit_transform(df["Stress"])
    X = df.drop(columns=["Stress"])
    y = df["Stress"]

    return X, y, label_encoder

# Train Test Split

def split_dataset(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_SEED,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


# Save Label Encoder

def save_label_encoder(label_encoder):

    joblib.dump(
        label_encoder,
        STRESS_LABEL_ENCODER_PATH
    )

    print("\nLabel Encoder Saved Successfully!")


# Main Function

def main():

    df = load_dataset()

    inspect_dataset(df)

    X, y, label_encoder = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    save_label_encoder(label_encoder)

    print("\nPreprocessing Completed Successfully!\n")

    print(f"Training Samples : {len(X_train)}")
    print(f"Testing Samples  : {len(X_test)}")

    print("\nTraining Class Distribution\n")
    print(y_train.value_counts())

    print("\nTesting Class Distribution\n")
    print(y_test.value_counts())

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    main()