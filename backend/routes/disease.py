import os

from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from backend.services.disease_service import detect_disease

disease_bp = Blueprint(
    "disease",
    __name__
)

UPLOAD_FOLDER = "backend/uploads"


@disease_bp.route(
    "/predict-disease",
    methods=["POST"]
)
def predict_disease():

    if "image" not in request.files:

        return jsonify(
            {
                "error": "No image uploaded"
            }
        ), 400

    image = request.files["image"]

    if image.filename == "":

        return jsonify(
            {
                "error": "No file selected"
            }
        ), 400

    plant_id = request.form.get(
        "plant_id",
        type=int
    )

    filename = secure_filename(
        image.filename
    )

    image_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    image.save(image_path)

    result = detect_disease(
        plant_id,
        image_path
    )

    return jsonify(result)