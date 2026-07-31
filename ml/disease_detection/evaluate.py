import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
)

from ml.config import (
    MODEL_DIR,
    MODEL_NAME,
)

from ml.disease_detection.preprocess import get_data_generators


def main():

    #Load Model
    model = load_model(f"{MODEL_DIR}/{MODEL_NAME}")

    #Validation Generator
    _, validation_generator = get_data_generators()

    #Evaluate Model
    loss, accuracy = model.evaluate(
        validation_generator,
        verbose=1
    )

    #Predictions
    predictions = model.predict(
        validation_generator,
        verbose=0
    )

    predicted_classes = np.argmax(predictions, axis=1)
    true_classes = validation_generator.classes

    #Calculate Metrics
    precision = precision_score(
        true_classes,
        predicted_classes,
        average="weighted"
    )

    recall = recall_score(
        true_classes,
        predicted_classes,
        average="weighted"
    )

    f1 = f1_score(
        true_classes,
        predicted_classes,
        average="weighted"
    )

    #Final Results
    print("\n MODEL EVALUATION RESULTS")
    print("*" * 40)

    print(f"Loss       : {loss:.4f}")
    print(f"Accuracy   : {accuracy:.4f}")
    print(f"Precision  : {precision:.4f}")
    print(f"Recall     : {recall:.4f}")
    print(f"F1 Score   : {f1:.4f}")


if __name__ == "__main__":
    main()