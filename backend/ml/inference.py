import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("models/gesture_model.h5")

labels = ["fist","open","peace","thumbs_up"]

def predict_gesture(features):

    features = np.array(features).reshape(1,1,42)

    pred = model.predict(features)

    index = pred.argmax()

    return labels[index]