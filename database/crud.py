import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import get_connection

def add_plant(plant_name, crop_type, location, date_planted):

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO plant
    (plant_name, crop_type, location, date_planted)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        plant_name,
        crop_type,
        location,
        date_planted
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return True

def save_sensor_reading(
    plant_id,
    soil_moisture,
    solar_radiation,
    air_temperature,
    relative_humidity,
    vpd
):

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO sensor_reading
    (
        plant_id,
        soil_moisture,
        solar_radiation,
        air_temperature,
        relative_humidity,
        vpd
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        plant_id,
        soil_moisture,
        solar_radiation,
        air_temperature,
        relative_humidity,
        vpd
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return True

def save_disease_prediction(plant_id, image_path, predicted_disease, confidence):

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO disease_prediction
    (plant_id, image_path, predicted_disease, confidence)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        plant_id,
        image_path,
        predicted_disease,
        confidence
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return True

def save_stress_prediction(
    plant_id,
    prediction_type,
    stress_level,
    confidence
):

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO stress_prediction
    (
        plant_id,
        prediction_type,
        stress_level,
        confidence
    )
    VALUES (%s, %s, %s, %s)
    """

    values = (
        plant_id,
        prediction_type,
        stress_level,
        confidence
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return True

def save_stress_forecast(
    plant_id,
    forecast_time,
    predicted_soil_moisture,
    predicted_solar_radiation,
    predicted_air_temperature,
    predicted_relative_humidity,
    predicted_vpd
):

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO stress_forecast
    (
        plant_id,
        forecast_time,
        predicted_soil_moisture,
        predicted_solar_radiation,
        predicted_air_temperature,
        predicted_relative_humidity,
        predicted_vpd
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        plant_id,
        forecast_time,
        predicted_soil_moisture,
        predicted_solar_radiation,
        predicted_air_temperature,
        predicted_relative_humidity,
        predicted_vpd
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return True

def save_irrigation_recommendation(
    plant_id,
    pump_duration_seconds,
    reason
):

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO irrigation_recommendation
    (plant_id, pump_duration_seconds, reason)
    VALUES (%s, %s, %s)
    """

    values = (
        plant_id,
        pump_duration_seconds,
        reason
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return True

def save_alert(plant_id, alert_type, message):

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO alert
    (plant_id, alert_type, message)
    VALUES (%s, %s, %s)
    """

    values = (
        plant_id,
        alert_type,
        message
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return True

def get_latest_sensor_reading(plant_id):

    connection = get_connection()

    if connection is None:
        return None

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM sensor_reading
    WHERE plant_id = %s
    ORDER BY time_stamp DESC
    LIMIT 1
    """

    cursor.execute(query, (plant_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result