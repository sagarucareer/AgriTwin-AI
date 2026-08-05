from flask import Blueprint
from flask import request
from flask import jsonify

from backend.services.forecast_service import predict_forecast

forecast_bp = Blueprint(
    "forecast",
    __name__
)


@forecast_bp.route(
    "/forecast-stress",
    methods=["POST"]
)
def forecast_stress_route():

    data = request.get_json()

    result = predict_forecast(
        data["plant_id"]
    )

    return jsonify(result)