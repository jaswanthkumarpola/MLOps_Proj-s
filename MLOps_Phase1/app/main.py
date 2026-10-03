from contextlib import asynccontextmanager
from pathlib import Path
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from app.schemas import PredictionRequest, PredictionResponse

MODEL_PATH = Path(__file__).resolve().parent / "model.joblib"
model = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    if not MODEL_PATH.exists():
        raise RuntimeError(f"Model artifact not found at {MODEL_PATH}")
    model = joblib.load(MODEL_PATH)
    yield
    # Cleanup logic (if any) when the server shuts down
    model = None

app = FastAPI(
    title="MLOps Model Serving Service",
    description="Production inference API powered by Scikit-Learn",
    version="0.2.0",
    lifespan=lifespan
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "model-serving",
        "model_loaded": model is not None
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not ready")

    # Format input into 2D array: shape (1, 2)
    features = np.array([[payload.square_footage, payload.bedrooms]])
    raw_prediction = model.predict(features)[0]

    return PredictionResponse(
        predicted_value=round(float(raw_prediction), 2),
        model_version="v0.2-scikit"
    )