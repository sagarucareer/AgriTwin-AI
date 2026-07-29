CREATE TABLE stress_forecast(
	forecast_id INT AUTO_INCREMENT PRIMARY KEY,
    plant_id INT NOT NULL,
    forecast_time DATETIME NOT NULL,
    predicted_stress ENUM('Low', 'Medium', 'High') NOT NULL,
    confidence DECIMAL(5, 2) NOT NULL,
    time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plant_id) REFERENCES plant(plant_id) ON DELETE CASCADE
);