'''
generate_dataset.py

├── Configuration
├── VPD Calculation
├── Time Period Detection
├── Weather Profiles
├── Sensor Simulation
├── Soil Stress
├── Temperature Stress
├── Humidity Stress
├── Solar Stress
├── VPD Stress
├── Final Stress Calculation
├── Dataset Generation
└── CSV Export
'''


#Part 1 
'''
Imports
Configuration
VPD calculation
Time-of-day classification
Weather profile generation
Realistic sensor data simulation
Sensor value clamping
'''

import math
import random
from datetime import datetime, timedelta
import pandas as pd

#CONFIGURATION
NUM_SAMPLES = 7500
TIME_INTERVAL = 5  # minutes
START_DATE = datetime(2026, 1, 1, 6, 0)

OUTPUT_PATH = "ml/datasets/stress_dataset/raw/stress_dataset.csv"

random.seed(42)


#VPD CALCULATION
def calculate_vpd(temperature, humidity):
    """
    Calculates Vapor Pressure Deficit (kPa)
    using Temperature (°C) and Relative Humidity (%)
    """

    saturation_vapor_pressure = (
        0.6108 *
        math.exp((17.27 * temperature) / (temperature + 237.3))
    )
    actual_vapor_pressure = (
        saturation_vapor_pressure *
        (humidity / 100)
    )
    vpd = saturation_vapor_pressure - actual_vapor_pressure
    #Cap VPD
    vpd = min(vpd, 3.5)
    return round(vpd, 2)


#TIME OF DAY
def get_time_period(hour):

    if 6 <= hour < 10:
        return "Morning"

    elif 10 <= hour < 16:
        return "Afternoon"

    elif 16 <= hour < 19:
        return "Evening"

    return "Night"


#DAILY WEATHER PROFILE
def get_weather_profile():

    profiles = [
        {
            "name": "Cloudy",
            "temp_offset": -3,
            "humidity_offset": 10,
            "solar_multiplier": 0.55
        },
        {
            "name": "Normal",
            "temp_offset": 0,
            "humidity_offset": 0,
            "solar_multiplier": 1.0
        },
        {
            "name": "Sunny",
            "temp_offset": 2,
            "humidity_offset": -8,
            "solar_multiplier": 1.15
        },
        {
            "name": "HotDry",
            "temp_offset": 5,
            "humidity_offset": -18,
            "solar_multiplier": 1.30
        }
    ]

    return random.choices(
        profiles,
        weights=[15, 50, 25, 10],
        k=1
    )[0]


#SENSOR SIMULATION
def generate_sensor_data(current_time, weather, current_soil):

    hour = current_time.hour + current_time.minute / 60

    #Temperature Curve
    temperature = (
        27
        + 8 * math.sin(math.pi * (hour - 6) / 12)
    )

    temperature += weather["temp_offset"]
    temperature += random.uniform(-1, 1)
    temperature = max(15, min(45, temperature))

    #Solar Radiation Curve
    solar = (
        100000 *
        max(
            0,
            math.sin(math.pi * (hour - 6) / 12)
        )
    )

    solar *= weather["solar_multiplier"]
    solar += random.uniform(-3000, 3000)
    solar = max(0, min(100000, solar))
    solar = int(solar)

    #Humidity Curve (Inverse of Temperature)
    humidity = (
        90
        - (temperature - 20) * 2.3
    )

    humidity += weather["humidity_offset"]
    humidity += random.uniform(-3, 3)
    humidity = max(20, min(95, humidity))

    #Soil Moisture Dynamics
    drying_rate = random.uniform(0.03, 0.08)

    if temperature > 32:
        drying_rate *= 1.5

    if solar > 70000:
        drying_rate *= 1.5

    if humidity < 40:
        drying_rate *= 1.3

    if solar > 70000:
        drying_rate *= 1.8

    elif solar > 40000:
        drying_rate *= 1.3

    current_soil -= drying_rate
    current_soil = max(15, current_soil)

    #Irrigation Event
    if current_soil < 40:
        if random.random() < 0.70:
            current_soil = random.uniform(75, 85)

    #Rain Event
    if weather["name"] == "Cloudy":
        if random.random() < 0.01:
            current_soil += random.uniform(5, 12)

    current_soil = max(15, min(90, current_soil))

    #VPD
    vpd = calculate_vpd(
        temperature,
        humidity
    )

    return (
        round(current_soil, 2),
        solar,
        round(temperature, 2),
        round(humidity, 2),
        vpd,
        current_soil
    )

#Part - 2
'''
Soil stress function
VPD stress function
Temperature stress
Solar radiation stress
Humidity stress
Final agronomic stress score
Low / Medium / High label generation
'''


#Soil Stress
def soil_stress(soil):

    if soil >= 70:
        return 0.0

    elif soil >= 50:
        return 0.3

    elif soil >= 35:
        return 0.6

    return 1.0


#VPD Stress
def vpd_stress(vpd):

    if vpd <= 1.2:
        return 0.0

    elif vpd <= 1.6:
        return 0.4

    elif vpd <= 2.0:
        return 0.7

    return 1.0


#Temperature Stress
def temperature_stress(temp):

    if 22 <= temp <= 28:
        return 0.0

    elif 28 < temp <= 32:
        return 0.4

    elif 32 < temp <= 36:
        return 0.7

    return 1.0


#Humidity Stress
def humidity_stress(humidity):

    if 60 <= humidity <= 80:
        return 0.0

    elif 45 <= humidity < 60:
        return 0.5

    elif humidity < 45:
        return 1.0

    return 0.3


#Solar Radiation Stress
def solar_stress(solar):

    if solar <= 30000:
        return 0.0

    elif solar <= 60000:
        return 0.4

    elif solar <= 80000:
        return 0.7

    return 1.0


#Calculate Final Stress
def calculate_stress(soil, temperature, humidity, solar, vpd):

    soil_score = soil_stress(soil)
    vpd_score = vpd_stress(vpd)
    temperature_score = temperature_stress(temperature)
    humidity_score = humidity_stress(humidity)
    solar_score = solar_stress(solar)
    stress_score = (
        0.40 * soil_score
        + 0.25 * vpd_score
        + 0.15 * temperature_score
        + 0.10 * humidity_score
        + 0.10 * solar_score
    )

    if stress_score < 0.25:
        return "Low"

    elif stress_score < 0.55:
        return "Medium"

    return "High"

#Part 3
'''
Dataset generation loop
Timestamp generation
Weather profile updates for each simulated day
Creating the Pandas DataFrame
Saving stress_dataset.csv
Printing dataset statistics (shape, class distribution, feature summary)
'''

#Main
def main():

    dataset = []
    current_time = START_DATE
    current_weather = get_weather_profile()
    current_day = current_time.date()
    current_soil = random.uniform(75, 85)

    for _ in range(NUM_SAMPLES):

        #Generate new weather profile for each day
        if current_time.date() != current_day:
            current_day = current_time.date()
            current_soil = random.uniform(75, 85)
            current_weather = get_weather_profile()

        (
            soil,
            solar,
            temperature,
            humidity,
            vpd,
            current_soil
        ) = generate_sensor_data(
            current_time,
            current_weather,
            current_soil
        )

        stress = calculate_stress(
            soil,
            temperature,
            humidity,
            solar,
            vpd
        )

        dataset.append({
            "Timestamp": current_time,
            "Soil_Moisture": soil,
            "Solar_Radiation": solar,
            "Air_Temperature": temperature,
            "Relative_Humidity": humidity,
            "VPD": vpd,
            "Stress": stress
        })

        current_time += timedelta(
            minutes=TIME_INTERVAL
        )

    df = pd.DataFrame(dataset)

    df.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print("\nDataset Generated Successfully!\n")
    print(f"Total Samples : {len(df)}")
    print("\nStress Distribution\n")
    print(df["Stress"].value_counts())
    print("\nFeature Statistics\n")
    print(df.describe())
    print(f"\nDataset saved to:\n{OUTPUT_PATH}")


if __name__ == "__main__":
    main()