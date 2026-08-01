import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from ml.config import (
    STRESS_RF_MODEL_PATH
)

from ml.stress_prediction.preprocess import (
    load_dataset,
    preprocess_data,
    split_dataset
)
from ml.config import STRESS_LABEL_ENCODER_PATH

#Load Model
def load_model():

    model = joblib.load(
        STRESS_RF_MODEL_PATH
    )

    return model


#Evaluate Model
def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )
    precision = precision_score(
        y_test,
        predictions,
        average="weighted"
    )
    recall = recall_score(
        y_test,
        predictions,
        average="weighted"
    )
    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    print("\nModel Evaluation\n")

    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")

    print("\nClassification Report\n")
    label_encoder = joblib.load(STRESS_LABEL_ENCODER_PATH)

    print(
        classification_report(
            y_test,
            predictions,
            target_names=label_encoder.classes_
        )
    )

    print("\nConfusion Matrix\n")
    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )

    return model.feature_importances_


# Feature Importance

def feature_importance(model, X):

    importance = pd.DataFrame(
        {
            "Feature": X.columns,
            "Importance": model.feature_importances_
        }
    )
    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    print("\nFeature Importance\n")
    print(importance)


#Main Function
def main():

    df = load_dataset()

    X, y, _ = preprocess_data(df)
    _, X_test, _, y_test = split_dataset(
        X,
        y
    )

    model = load_model()

    evaluate_model(
        model,
        X_test,
        y_test
    )
    feature_importance(
        model,
        X
    )


if __name__ == "__main__":
    main()