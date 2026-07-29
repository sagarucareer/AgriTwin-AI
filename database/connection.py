import mysql.connector
from config.database import DB_CONFIG


def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            return connection

    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")

    return None