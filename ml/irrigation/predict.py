from ml.irrigation.irrigation_pipeline import (
    irrigation_decision
)

#Sample Inputs
current_stress = "Medium"
future_stress = "High"
current_soil_moisture = 52.8
future_soil_moisture = 41.3
current_vpd = 1.85
future_vpd = 2.46

decision = irrigation_decision(

    current_stress,
    future_stress,

    current_soil_moisture,
    future_soil_moisture,

    current_vpd,
    future_vpd

)

print("\nIrrigation Decision\n")

print(f"Current Stress        : {current_stress}")
print(f"Future Stress         : {future_stress}")

print(f"\nCurrent Soil Moisture : {current_soil_moisture:.2f} %")
print(f"Future Soil Moisture  : {future_soil_moisture:.2f} %")

print(f"\nCurrent VPD           : {current_vpd:.2f} kPa")
print(f"Future VPD            : {future_vpd:.2f} kPa")

print("\nDecision\n")

print(
    f"Irrigation Required : "
    f"{'YES' if decision['irrigation_required'] else 'NO'}"
)

print(
    f"Pump Duration       : "
    f"{decision['pump_duration']} seconds"
)

print(
    f"Reason              : "
    f"{decision['reason']}"
)