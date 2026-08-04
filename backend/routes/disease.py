from flask import Blueprint

disease_bp = Blueprint("disease", __name__)


@disease_bp.route("/predict-disease", methods=["POST"])
def predict_disease():
    return {
        "message": "Disease Prediction API Working"
    }