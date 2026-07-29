CREATE TABLE irrigation_recommendation(
	recommendation_id INT AUTO_INCREMENT PRIMARY KEY,
    plant_id INT NOT NULL,
    recommended_water_ml DECIMAL(8, 2) NOT NULL,
    reason VARCHAR(255),
    time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(plant_id) REFERENCES plant(plant_id) ON DELETE CASCADE
);