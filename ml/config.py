#Disease Detection Dataset
DISEASE_DATASET_DIR = "ml/datasets/disease_dataset/raw"

#Image configuration
IMAGE_SIZE = (300, 300)

#Training configuration
BATCH_SIZE = 32

INITIAL_EPOCHS = 10
FINE_TUNE_EPOCHS = 20

INITIAL_LR = 1e-3
FINE_TUNE_LR = 1e-5

VALIDATION_SPLIT = 0.20

#Model paths
MODEL_DIR = "ml/models"
MODEL_NAME = "best_disease_detector.keras"

#Prediction configuration
CONFIDENCE_THRESHOLD = 0.5

#Reproducibility
RANDOM_SEED = 42

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

# ***************************************************************************

#Stress Prediction Dataset
STRESS_DATASET_PATH = "ml/datasets/stress_dataset/raw/stress_dataset.csv"


#Stress Prediction Models
LABEL_ENCODER_PATH = "ml/models/stress_label_encoder.pkl"
STRESS_RF_MODEL_PATH = "ml/models/stress_random_forest.pkl"
STRESS_LABEL_ENCODER_PATH = "ml/models/stress_label_encoder.pkl"
SCALER_PATH = "ml/models/stress_scaler.pkl"

#Stress Prediction Configuration
TEST_SIZE = 0.20

# ***************************************************************************

#Stress Forecasting Model
STRESS_LSTM_MODEL_PATH = "ml/models/stress_lstm.keras"

SEQUENCE_LENGTH = 24
LSTM_BATCH_SIZE = 32
LSTM_EPOCHS = 30
LSTM_LEARNING_RATE = 1e-3

LSTM_UNITS_1 = 64
LSTM_UNITS_2 = 32

DROPOUT_RATE = 0.2

DENSE_UNITS = 32

# ***************************************************************************

#Report paths
REPORT_DIR = "ml/reports"
