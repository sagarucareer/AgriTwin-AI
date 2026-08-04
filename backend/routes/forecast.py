from flask import Blueprint

forecast_bp = Blueprint("forecast", __name__)


@forecast_bp.route("/forecast-stress", methods=["POST"])
def forecast_stress():
    return {
        "message": "Stress Forecast API Working"
    }