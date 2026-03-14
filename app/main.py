from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.schemas import ImageInput
from app.model import predict_digit
from app.preprocess import preprocess_base64_image

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
def root():
    return FileResponse("frontend/index.html")