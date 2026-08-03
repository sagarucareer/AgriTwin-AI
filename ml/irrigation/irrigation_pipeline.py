import numpy as np

#Irrigation Decision
def irrigation_decision(
    current_stress,
    future_stress,

    current_soil_moisture,
    future_soil_moisture,

    current_vpd,
    future_vpd
):

    #Default Values
    irrigation_required = False
    pump_duration = 0
    reason = "No irrigation required."

    if future_stress == "High":

        irrigation_required = True
        pump_duration = 300
        reason = "High stress predicted in the next cycle."

    elif current_stress == "High":

        irrigation_required = True
        pump_duration = 240
        reason = "Plant is currently under high stress."

    elif future_soil_moisture < 45:

        irrigation_required = True
        pump_duration = 240
        reason = "Future soil moisture predicted below safe level."

    elif future_vpd > 2.2:

        irrigation_required = True
        pump_duration = 180
        reason = "High future VPD may increase plant water loss."

    elif future_stress == "Medium":

        irrigation_required = True
        pump_duration = 120
        reason = "Moderate stress predicted in the next cycle."

    return {
        "irrigation_required": irrigation_required,
        "pump_duration": pump_duration,
        "reason": reason
    }