from flask import Blueprint
from flask import request
from flask import jsonify

from backend.services.stress_service import detect_stress

stress_bp = Blueprint(
    "stress",
    __name__
)


@stress_bp.route(
    "/predict-stress",
    methods=["POST"]
)
def predict_stress_route():

    data = request.get_json()

    result = detect_stress(

        plant_id=data["plant_id"],

        soil_moisture=data["soil_moisture"],

        solar_radiation=data["solar_radiation"],

        air_temperature=data["air_temperature"],

        relative_humidity=data["relative_humidity"],

        vpd=data["vpd"]

    )

    return jsonify(result)