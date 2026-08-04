import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from database.crud import get_latest_sensor_reading


def get_dashboard_data():

    sensor = get_latest_sensor_reading(1)

    return sensor