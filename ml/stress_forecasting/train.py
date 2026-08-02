import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    LSTM,
    Dense,
    Dropout
)
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint
)
from ml.config import (
    STRESS_LSTM_MODEL_PATH,
    LSTM_UNITS_1,
    LSTM_UNITS_2,
    DENSE_UNITS,
    DROPOUT_RATE,
    LSTM_BATCH_SIZE,
    LSTM_EPOCHS,
    LSTM_LEARNING_RATE
)
from ml.stress_forecasting.preprocess import (
    load_dataset,
    preprocess_data,
    create_sequences,
    split_dataset
)

#Build Model
def build_model(input_shape):

    model = Sequential(
        [
            LSTM(LSTM_UNITS_1, return_sequences=True, input_shape=input_shape),
            Dropout(DROPOUT_RATE),
            LSTM(LSTM_UNITS_2),
            Dense(DENSE_UNITS, activation="relu"),
            Dense(5)
        ]
    )

    model.compile(
        optimizer=Adam(
            learning_rate=LSTM_LEARNING_RATE
        ),
        loss="mse",
        metrics=["mae"]
    )

    return model

#Train Model
def train_model(model, X_train, y_train):

    history = model.fit(
        X_train,
        y_train,
        validation_split=0.2,
        epochs=LSTM_EPOCHS,
        batch_size=LSTM_BATCH_SIZE,
        callbacks=[
            ModelCheckpoint(
                filepath=STRESS_LSTM_MODEL_PATH,
                monitor="val_loss",
                save_best_only=True
            ),
            EarlyStopping(
                monitor="val_loss",
                patience=5,
                restore_best_weights=True
            )
        ],
        verbose=1
    )

    return history

#Main Function
def main():

    df = load_dataset()
    scaled_data, _ = preprocess_data(df)

    X, y = create_sequences(scaled_data)
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    model = build_model(
        (
            X_train.shape[1],
            X_train.shape[2]
        )
    )

    print("\nTraining Configuration\n")

    print(f"Epochs       : {LSTM_EPOCHS}")
    print(f"Batch Size   : {LSTM_BATCH_SIZE}")
    print(f"Learning Rate: {LSTM_LEARNING_RATE}")

    print("\nLSTM Model Summary\n")

    model.summary()

    train_model(model, X_train, y_train)

    print("\nTraining Completed Successfully!")
    print(f"\nModel Saved To : {STRESS_LSTM_MODEL_PATH}")


if __name__ == "__main__":
    main()