from flask import Blueprint

from backend.services.dashboard_service import get_dashboard_data

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():

    data = get_dashboard_data()

    return data