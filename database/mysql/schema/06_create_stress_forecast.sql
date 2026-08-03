CREATE TABLE stress_forecast(
	forecast_id INT AUTO_INCREMENT PRIMARY KEY,
    plant_id INT NOT NULL,
    forecast_time DATETIME NOT NULL,
    predicted_stress ENUM('Low', 'Medium', 'High') NOT NULL,
    confidence DECIMAL(5, 2) NOT NULL,
    time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plant_id) REFERENCES plant(plant_id) ON DELETE CASCADE
);

ALTER TABLE stress_forecast
ADD COLUMN predicted_soil_moisture FLOAT NOT NULL AFTER forecast_time,
ADD COLUMN predicted_solar_radiation FLOAT NOT NULL AFTER predicted_soil_moisture,
ADD COLUMN predicted_air_temperature FLOAT NOT NULL AFTER predicted_solar_radiation,
ADD COLUMN predicted_relative_humidity FLOAT NOT NULL AFTER predicted_air_temperature,
ADD COLUMN predicted_vpd FLOAT NOT NULL AFTER predicted_relative_humidity;

ALTER TABLE stress_forecast
DROP COLUMN predicted_stress,
DROP COLUMN confidence;