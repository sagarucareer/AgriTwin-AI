import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import get_connection

try:
    connection = get_connection()
    if connection.is_connected():
        print("Connected to MYSQL successfully!")
    connection.close()
    print("Connection closed!")
except Exception as e:
    print("Error: ", e)