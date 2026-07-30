import tensorflow as tf

from tensorflow.keras.applications import EfficientNetB3
from tensorflow.keras.layers import (
    Dense,
    GlobalAveragePooling2D,
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
    LEARNING_RATE,
    EPOCHS,
    MODEL_DIR,
    MODEL_NAME,
)

from ml.disease_detection.preprocess import get_data_generators

def main():
    
    #Load Dataset
    train_generator, validation_generator = get_data_generators()

    #Build Base Model
    base_model = EfficientNetB3(
        weights="imagenet",
        include_top=False,
        input_shape=(*IMAGE_SIZE, 3),
    )

    #Freeze all layers
    base_model.trainable = False

    #Classification Head
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = BatchNormalization()(x)
    x = Dense(256, activation="relu")(x)
    x = Dropout(0.4)(x)
    x = Dense(64, activation="relu")(x)
    x = Dropout(0.3)(x)
    output = Dense(train_generator.num_classes, activation="softmax")(x)

    #Create Model
    model = Model(
        inputs=base_model.input,
        outputs=output
    )

    #Compile Model
    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=LEARNING_RATE
        ),
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    #Model Summary
    model.summary()

    print("\n******** Training Configuration ********")
    print(f"Image Size     : {IMAGE_SIZE}")
    print(f"Epochs         : {EPOCHS}")
    print(f"Learning Rate  : {LEARNING_RATE}")
    print(f"Classes        : {train_generator.num_classes}")
    print("***************************************\n")

    #Callbacks
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
            patience=6,
            restore_best_weights=True,
            verbose=1
        ),
        ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.2,
            patience=3,
            min_lr=1e-6,
            verbose=1
        )
    ]

    #Train Model
    history = model.fit(
        train_generator,
        validation_data=validation_generator,
        epochs=EPOCHS,
        callbacks=callbacks
    )

    #Save Final Model
    model.save(
        f"{MODEL_DIR}/disease_detector_final.keras"
    )

    print("\n✅ Training completed successfully.")
    print(f"📁 Best model saved to: {MODEL_DIR}/{MODEL_NAME}")
    print(f"📁 Final model saved to: {MODEL_DIR}/disease_detector_final.keras")

if __name__ == "__main__":
    main()