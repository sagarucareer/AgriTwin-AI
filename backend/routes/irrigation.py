from flask import Blueprint

irrigation_bp = Blueprint("irrigation", __name__)


@irrigation_bp.route("/irrigation", methods=["GET"])
def irrigation():
    return {
        "message": "Irrigation Recommendation API Working"
    }