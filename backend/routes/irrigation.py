from flask import Blueprint
from flask import jsonify
from flask import request

from backend.services.irrigation_service import (
    get_irrigation_recommendation
)

irrigation_bp = Blueprint(
    "irrigation",
    __name__
)


@irrigation_bp.route(
    "/recommend-irrigation",
    methods=["POST"]
)
def recommend():

    data = request.get_json()

    result = get_irrigation_recommendation(

        plant_id=data["plant_id"],

        current_stress=data["current_stress"],
        future_stress=data["future_stress"],

        current_soil_moisture=data["current_soil_moisture"],
        future_soil_moisture=data["future_soil_moisture"],

        current_vpd=data["current_vpd"],
        future_vpd=data["future_vpd"]

    )

    return jsonify(result)