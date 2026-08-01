import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from ml.config import (
    STRESS_RF_MODEL_PATH,
    RANDOM_SEED
)

from ml.stress_prediction.preprocess import (
    load_dataset,
    preprocess_data,
    split_dataset
)


#Train Model
def train_model(X_train, y_train):

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=12,
        random_state=RANDOM_SEED,
        n_jobs=-1
    )
    model.fit(
        X_train,
        y_train
    )

    return model


#Save Model
def save_model(model):

    joblib.dump(
        model,
        STRESS_RF_MODEL_PATH
    )

    print("\nModel Saved Successfully!")

#Main Function
def main():

    df = load_dataset()

    X, y, _ = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_dataset(
        X,
        y
    )

    model = train_model(
        X_train,
        y_train
    )

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_accuracy = accuracy_score(
        y_train,
        train_predictions
    )
    test_accuracy = accuracy_score(
        y_test,
        test_predictions
    )

    print("\nTraining Completed Successfully!")

    print(f"\nTraining Accuracy : {train_accuracy:.4f}")
    print(f"Testing Accuracy  : {test_accuracy:.4f}")

    print("\nRandom Forest Configuration")

    print(f"Number of Trees : {model.n_estimators}")
    print(f"Maximum Depth   : {model.max_depth}")

    save_model(model)


if __name__ == "__main__":
    main()