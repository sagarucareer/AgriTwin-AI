CREATE TABLE alert(
	alert_id INT AUTO_INCREMENT PRIMARY KEY,
    plant_id INT NOT NULL,
    alset_type VARCHAR(50) NOT NULL,
    message VARCHAR(255) NOT NULL,
    time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plant_id) REFERENCES plant(plant_id) ON DELETE CASCADE
);

ALTER TABLE alert
RENAME COLUMN alset_type TO alert_type;