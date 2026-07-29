SELECT * FROM plant;

SELECT * FROM sensor_reading;

SELECT * FROM disease_prediction;

SELECT * FROM stress_prediction;

SELECT * FROM stress_forecast;

SELECT * FROM irrigation_recommendation;

SELECT * FROM alert;

SELECT AVG(soil_moisture) FROM sensor_reading
WHERE plant_id = 1;

SELECT * FROM sensor_reading
ORDER BY time_stamp DESC
LIMIT 1;