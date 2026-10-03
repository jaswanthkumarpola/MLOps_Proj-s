from fastapi.testclient import TestClient
from app.main import app

def test_health_endpoint():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
        assert response.json()["model_loaded"] is True

def test_prediction_valid():
    with TestClient(app) as client:
        payload = {"square_footage": 1200.0, "bedrooms": 2}
        response = client.post("/predict", json=payload)
        assert response.status_code == 200
        assert "predicted_value" in response.json()
        assert response.json()["model_version"] == "v0.2-scikit"

def test_prediction_invalid_square_footage():
    with TestClient(app) as client:
        payload = {"square_footage": -50.0, "bedrooms": 2}
        response = client.post("/predict", json=payload)
        assert response.status_code == 422