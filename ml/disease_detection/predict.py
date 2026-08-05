import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from ml.config import (
    IMAGE_SIZE,
    MODEL_DIR,
    MODEL_NAME,
    CLASS_NAMES,
)

def predict_image(image_path):

    #Load model
    model = load_model(
        f"{MODEL_DIR}/{MODEL_NAME}"
    )

    #Load image
    img = image.load_img(
        image_path,
        target_size=IMAGE_SIZE
    )

    #Convert Image to Numpy
    img_array = image.img_to_array(img)

    #Normalize
    img_array /= 255.0

    #Batch Dimension
    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    #Prediction
    prediction = model.predict(
        img_array,
        verbose=0
    )

    #Highest Prediction
    predicted_index = np.argmax(prediction)

    #Confidence
    confidence = float(
        prediction[0][predicted_index] * 100
    )

    #Predicted Disease
    disease = CLASS_NAMES[predicted_index]

    #Display prediction
    # print("\n******** PREDICTION ********")
    # print(f"Disease   : {disease}")
    # print(f"Confidence: {confidence:.2f}%")

    return disease, confidence


if __name__ == "__main__":

    image_path = input("Enter image path: ")

    predict_image(image_path)