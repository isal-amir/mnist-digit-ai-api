import numpy as np
import tflite_runtime.interpreter as tflite

from app.config import MODEL_PATH

interpreter = tflite.Interpreter(model_path=str(MODEL_PATH))
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()



def predict_digit(img):

    img = img.astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], img)

    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]['index'])

    probs = output[0]

    digit = int(np.argmax(probs))

    return digit, probs.tolist()
