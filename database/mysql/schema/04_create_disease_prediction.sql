CREATE TABLE disease_prediction(
	prediction_id INT AUTO_INCREMENT PRIMARY KEY,
    plant_id INT NOT NULL,
    image_path VARCHAR(100) NOT NULL,
    confidence DECIMAL(5, 2) NOT NULL,
    time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plant_id) REFERENCES plant(plant_id) ON DELETE CASCADE
);

ALTER TABLE disease_prediction
ADD predicted_disease VARCHAR(100) NOT NULL;