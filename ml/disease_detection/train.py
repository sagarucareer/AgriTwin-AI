import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB3
from tensorflow.keras.layers import (
    GlobalAveragePooling2D,
    Dense,
    BatchNormalization,
    Dropout,
)
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import (
    ModelCheckpoint,
    EarlyStopping,
    ReduceLROnPlateau,
)
from ml.config import (
    IMAGE_SIZE,
    INITIAL_LR,
    FINE_TUNE_LR,
    INITIAL_EPOCHS,
    FINE_TUNE_EPOCHS,
    MODEL_DIR,
    MODEL_NAME,
)
from ml.disease_detection.preprocess import get_data_generators

def main():

    #Load Dataset
    train_generator, validation_generator = get_data_generators()

    #Build EfficientNetB3
    base_model = EfficientNetB3(
        include_top=False,
        weights="imagenet",
        input_shape=(*IMAGE_SIZE, 3)
    )

    #Freeze entire backbone
    base_model.trainable = False

    #Classification Head
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = BatchNormalization()(x)
    x = Dense(512,activation="relu")(x)
    x = Dropout(0.5)(x)
    x = Dense(256,activation="relu")(x)
    x = Dropout(0.3)(x)
    output = Dense(train_generator.num_classes, activation="softmax")(x)

    model = Model(
        inputs=base_model.input,
        outputs=output
    )

    #Compile Stage 1
    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=INITIAL_LR
        ),
        loss=tf.keras.losses.CategoricalCrossentropy(
            label_smoothing=0.1
        ),
        metrics=["accuracy"]
    )

    model.summary()

    callbacks = [
        ModelCheckpoint(
            filepath=f"{MODEL_DIR}/{MODEL_NAME}",
            monitor="val_accuracy",
            save_best_only=True,
            mode="max",
            verbose=1
        ),
        EarlyStopping(
            monitor="val_loss",
            patience=5,
            restore_best_weights=True,
            verbose=1
        ),
        ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.2,
            patience=2,
            verbose=1
        )
    ]

    #Training
    model.fit(
        train_generator,
        validation_data=validation_generator,
        epochs=INITIAL_EPOCHS,
        callbacks=callbacks
    )

    #Fine Tuning
    base_model.trainable = True

    for layer in base_model.layers[:-30]:
        layer.trainable = False

    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=FINE_TUNE_LR
        ),
        loss=tf.keras.losses.CategoricalCrossentropy(
            label_smoothing=0.1
        ),
        metrics=["accuracy"]
    )

    #Training
    model.fit(
        train_generator,
        validation_data=validation_generator,
        initial_epoch=INITIAL_EPOCHS,
        epochs=INITIAL_EPOCHS + FINE_TUNE_EPOCHS,
        callbacks=callbacks
    )
    
    #Save Final Model
    model.save(
        f"{MODEL_DIR}/disease_detector_final.keras"
    )

    print("\n Training completed successfully.")
    print(f" Best model : {MODEL_DIR}/{MODEL_NAME}")
    print(f" Final model: {MODEL_DIR}/disease_detector_final.keras")


if __name__ == "__main__":
    main()