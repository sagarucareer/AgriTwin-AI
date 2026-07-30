#Dataset paths
DATASET_DIR = "ml/datasets/disease_dataset/raw"

#Model paths
MODEL_DIR = "ml/models"
MODEL_NAME = "best_disease_detector.keras"

#Image configuration
IMAGE_SIZE = (300, 300)

#Training configuration
BATCH_SIZE = 64
EPOCHS = 40
LEARNING_RATE = 3e-5
VALIDATION_SPLIT = 0.20

#Prediction configuration
CONFIDENCE_THRESHOLD = 0.5

#Reproducibility
RANDOM_SEED = 42

# Report Paths
REPORT_DIR = "ml/reports"