import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
)

from ml.disease_detection.predict import predict_image
from database.crud import save_disease_prediction
from database.crud import save_alert



def detect_disease(plant_id, image_path):

    disease, confidence = predict_image(image_path)

    save_disease_prediction(
        plant_id=plant_id,
        image_path=image_path,
        predicted_disease=disease,
        confidence=confidence
    )

    if disease != "Healthy":
        save_alert(
            plant_id=plant_id,
            alert_type="Disease",
            message=f"{disease} detected."
        )

    return {
        "predicted_disease": disease,
        "confidence": round(confidence, 2)
    }