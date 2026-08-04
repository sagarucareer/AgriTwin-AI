-- Plant Table
INSERT INTO plant(plant_name, crop_type, location, date_planted)
VALUES('Tomato Plant A', 'Tomato', 'Greenhouse 1', '2026-07-25');

-- Sesnor reading table
INSERT INTO sensor_reading
(
    plant_id,
    soil_moisture,
    solar_radiation,
    air_temperature,
    relative_humidity,
    vpd
)
VALUES
(1, 41.8, 28500.0, 30.5, 72.0, 1.21),
(1, 39.2, 30200.0, 31.1, 70.5, 1.34),
(1, 44.6, 27850.0, 29.8, 74.1, 1.10);

-- Disease Prediction
INSERT INTO disease_prediction(plant_id, image_path, predicted_disease, confidence)
Values
(1, 'uploads/tomato_leaf_001.jpg', 'Healthy', 98.42);

-- Current Stress Prediction
INSERT INTO stress_prediction(plant_id, prediction_type, stress_level, confidence)
VALUES(1, 'Current', 'Low', 96.81);

-- Future Sensor Forecast (LSTM)
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
VALUES(1, '2026-07-26 10:00:00', 38.4, 31500.0, 31.8, 68.7, 1.48);

-- Future Stress Prediction
-- (Generated using Random Forest on LSTM output)
INSERT INTO stress_prediction
(
    plant_id,
    prediction_type,
    stress_level,
    confidence
)
VALUES(1, 'Forecast', 'Medium', 91.63);

-- Irrigation Recommendation
INSERT INTO irrigation_recommendation(plant_id, pump_duration_seconds, reason)
VALUES(1, 180, 'Forecasted soil moisture is below threshold and future stress is Medium.');

-- Alert
INSERT INTO alert(plant_id, alert_type, message)
VALUES(1, 'Stress', 'Medium stress predicted for tomorrow');