import numpy as np
import tensorflow as tf

from app.config import MODEL_PATH

model = tf.keras.models.load_model(MODEL_PATH)


def predict_digit(img):

    pred = model.predict(img)

    probs = pred[0]

    digit = int(np.argmax(probs))

    return digit, probs.tolist()