from flask import Blueprint
from flask import jsonify
from flask import request

from backend.services.dashboard_service import (
    get_dashboard_data
)

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route(
    "/dashboard",
    methods=["GET"]
)
def dashboard():

    plant_id = request.args.get(
        "plant_id",
        type=int
    )

    result = get_dashboard_data(
        plant_id
    )

    return jsonify(result)