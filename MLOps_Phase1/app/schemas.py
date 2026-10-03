from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    # Simulating house price prediction features
    square_footage: float = Field(..., gt=0, description="Area in sq ft must be strictly positive")
    bedrooms: int = Field(..., ge=1, le=20, description="Number of bedrooms (1 to 20)")

class PredictionResponse(BaseModel):
    predicted_value: float
    model_version: str