import base64
import io
import numpy as np
from PIL import Image

from app.config import IMAGE_SIZE

#import matplotlib.pyplot as plt

def crop_image(img):

    coords = np.column_stack(np.where(img > 0))

    if coords.shape[0] == 0:
        return img

    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)

    cropped = img[y_min:y_max+1, x_min:x_max+1]

    return cropped


def preprocess_base64_image(image_base64: str):

    image_data = image_base64.split(",")[1]

    image_bytes = base64.b64decode(image_data)

    img = Image.open(io.BytesIO(image_bytes)).convert("L")

    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))

    img = np.array(img)

    # invert warna
    # img = 255 - img

    # crop
    img = crop_image(img)

    # resize
    img = Image.fromarray(img)
    img = img.resize((28,28))

    # konversi balik ke np.array
    img = np.array(img)

    img = img / 255.0

    img = img.reshape(1, 28, 28, 1)

    # debug
    # plt.imshow(img.squeeze(), cmap='gray')
    # plt.title("Preprocessed Image")
    # plt.show()

    return img

