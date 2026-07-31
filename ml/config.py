#Dataset paths
DATASET_DIR = "ml/datasets/disease_dataset/raw"

#Model paths
MODEL_DIR = "ml/models"
MODEL_NAME = "best_disease_detector.keras"

#Image configuration
IMAGE_SIZE = (300, 300)

#Training configuration
BATCH_SIZE = 32

INITIAL_EPOCHS = 10
FINE_TUNE_EPOCHS = 20

INITIAL_LR = 1e-3
FINE_TUNE_LR = 1e-5

VALIDATION_SPLIT = 0.20

#Prediction configuration
CONFIDENCE_THRESHOLD = 0.5

#Reproducibility
RANDOM_SEED = 42

#Report paths
REPORT_DIR = "ml/reports"

#Class names
CLASS_NAMES = [
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy",
]