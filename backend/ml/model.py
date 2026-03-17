import tensorflow as tf
from keras import Sequential, layers
from keras.layers import LSTM, Dense

def create_model(input_shape, num_classes):

    model = Sequential([
        layers.Input(shape=input_shape),
        LSTM(64,return_sequences=True),
        LSTM(32),
        Dense(64,activation='relu'),
        Dense(num_classes,activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model