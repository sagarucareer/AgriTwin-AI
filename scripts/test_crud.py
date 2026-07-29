import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.crud import (
    add_plant,
    save_sensor_reading,
    get_latest_sensor_reading
)


print("Adding Plant...")

add_plant(
    "Tomato Plant B",
    "Tomato",
    "Greenhouse 2",
    "2026-07-30"
)

print("Plant Added Successfully!")


print("\nSaving Sensor Reading...")

save_sensor_reading(
    2,
    31.4,
    68.7,
    42.1
)

print("Sensor Reading Saved!")


print("\nFetching Latest Sensor Reading...")

reading = get_latest_sensor_reading(2)

print(reading)