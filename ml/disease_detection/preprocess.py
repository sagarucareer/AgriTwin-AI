from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from ml.config import *

def get_data_generators():

    #Training Data Generator
    train_datagen = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        validation_split=VALIDATION_SPLIT,
        rotation_range=15,
        zoom_range=0.15,
        width_shift_range=0.10,
        height_shift_range=0.10,
        horizontal_flip=True
    )

    #Validation Data Generator
    validation_datagen = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        validation_split=VALIDATION_SPLIT
    )

    #Training Generator
    train_generator = train_datagen.flow_from_directory(
        DATASET_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="training",
        shuffle=True,
        seed=RANDOM_SEED
    )

    #Validation Generator
    validation_generator = validation_datagen.flow_from_directory(
        DATASET_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="validation",
        shuffle=False,
        seed=RANDOM_SEED
    )

    return train_generator, validation_generator


if __name__ == "__main__":

    train_generator, validation_generator = get_data_generators()

    print("\n************** Dataset Summary **************")
    print(f"Training Images   : {train_generator.samples}")
    print(f"Validation Images : {validation_generator.samples}")
    print(f"Number of Classes : {train_generator.num_classes}")

    print("\nClasses:")
    for class_name, class_index in train_generator.class_indices.items():
        print(f"{class_index:2d} -> {class_name}")
