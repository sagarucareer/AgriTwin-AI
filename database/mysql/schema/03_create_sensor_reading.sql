CREATE TABLE sensor_reading(
	reading_id INT AUTO_INCREMENT PRIMARY KEY,
	plant_id INT NOT NULL,
    temperature DECIMAL(5, 2) NOT NULL,
    humidity DECIMAL(5, 2) NOT NULL,
    soil_moisture DECIMAL(5, 2) NOT NULL,
    time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(plant_id) REFERENCES plant(plant_id) ON DELETE CASCADE
);