CREATE TABLE stress_prediction (
	stress_id INT AUTO_INCREMENT PRIMARY KEY,
    plant_id INT NOT NULL,
    stress_level ENUM('Low', 'Medium', 'High') NOT NULL,
    confidence DECIMAL(5, 2) NOT NULL,
    times_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(plant_id) REFERENCES plant(plant_id) ON DELETE CASCADE
);

ALTER TABLE stress_prediction
ADD COLUMN prediction_type
ENUM('Current','Forecast')
NOT NULL
DEFAULT 'Current'
AFTER plant_id;