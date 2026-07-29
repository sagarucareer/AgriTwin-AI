CREATE TABLE plant(
	plant_id INT AUTO_INCREMENT PRIMARY KEY,
    plant_name VARCHAR(100) NOT NULL,
    crop_type VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    date_planted DATE,
    STATUS ENUM('Active', 'Inactive', 'Harvested') DEFAULT 'Active'
);