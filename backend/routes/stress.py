from flask import Blueprint

stress_bp = Blueprint("stress", __name__)


@stress_bp.route("/predict-stress", methods=["POST"])
def predict_stress():
    return {
        "message": "Stress Prediction API Working"
    }