INSERT INTO plant(plant_name, crop_type, location, date_planted)
VALUES('Tomato Plant A', 'Tomato', 'Greenhouse 1', '2026-07-25');

INSERT INTO sensor_reading(plant_id, temperature, humidity, soil_moisture)
VALUES(1, 30.5, 72.0, 41.8),
(1, 31.1, 70.5, 39.2),
(1, 29.8, 74.1, 44.6);

INSERT INTO disease_prediction(plant_id, image_path, predicted_disease, confidence)
Values
(1, 'uploads/tomato_leaf_001.jpg', 'Healthy', 98.42);

INSERT INTO stress_prediction(plant_id, stress_level, confidence)
VALUES(1, 'Low', 96.81);

INSERT INTO stress_forecast(plant_id, forecast_time, predicted_stress, confidence)
VALUES(1, '2026-07-26 10:00:00', 'Medium', 91.63);

INSERT INTO irrigation_recommendation(plant_id, recommended_water_ml, reason)
VALUES(1, 250, 'Soil moisture below thresohld');

INSERT INTO alert(plant_id, alert_type, message)
VALUES(1, 'Stress', 'Medium stress predicted for tomorrow');