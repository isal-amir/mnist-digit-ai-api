from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent 

MODEL_PATH = BASE_DIR / "models" / "mnist.tflite"

IMAGE_SIZE = 28