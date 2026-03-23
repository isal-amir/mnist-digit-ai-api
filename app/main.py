import time

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.schemas import ImageInput
from app.model import predict_digit
from app.preprocess import preprocess_base64_image

app = FastAPI(
    title="MNIST Digit Recognition API",
    version="1.0"
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
def root():
    return FileResponse("frontend/index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: ImageInput):

    start = time.time()

    img = preprocess_base64_image(data.image)

    prediction, probs = predict_digit(img)

    latency = time.time() - start

    return {
        "prediction": prediction,
        "probabilities": probs,
        "latency": latency
    }