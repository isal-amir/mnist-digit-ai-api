from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent 

MODEL_PATH = BASE_DIR / "models" / "MNIST-model.keras"

IMAGE_SIZE = 28