from tensorflow.keras.preprocessing.image import ImageDataGenerator

from ml.config import (
    DATASET_DIR,
    IMAGE_SIZE,
    BATCH_SIZE,
    VALIDATION_SPLIT,
    RANDOM_SEED,
)


def get_data_generators():

    #Training Data Generator
    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255,
        validation_split=VALIDATION_SPLIT,
        rotation_range=25, #Data Augmentation
        zoom_range=0.20,
        width_shift_range=0.15,
        height_shift_range=0.15,
        brightness_range=(0.8, 1.2),
        horizontal_flip=True,
        fill_mode="nearest"
    )

    #Validation Data Generator
    validation_datagen = ImageDataGenerator(
        rescale=1.0 / 255,
        validation_split=VALIDATION_SPLIT
    )

    #Training Generator
    train_generator = train_datagen.flow_from_directory(
        directory=DATASET_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="training",
        shuffle=True,
        seed=RANDOM_SEED
    )

    #Validation Generator
    validation_generator = validation_datagen.flow_from_directory(
        directory=DATASET_DIR,
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