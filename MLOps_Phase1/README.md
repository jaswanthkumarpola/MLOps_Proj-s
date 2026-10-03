# MLOps Phase 1: Model Serving API

> **Note:** 🌱 This is my very first MLOps project! It serves as a foundational step into machine learning operations.

This project demonstrates a fundamental MLOps workflow: training a simple machine learning model (Linear Regression) and serving it via a RESTful API. The API is built using **FastAPI** and is containerized using **Docker** and **Docker Compose**.

## Project Structure

```text
MLOps_Phase1/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI application and endpoints
│   ├── schemas.py         # Pydantic models for request/response validation
│   └── model.joblib       # Serialized Scikit-Learn model (generated after training)
├── tests/
│   ├── __init__.py
│   └── test_main.py       # Pytest test cases for the API endpoints
├── train.py               # Script to train and save the model
├── Dockerfile             # Docker configuration for the API
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Prerequisites
- Python 3.12+
- Docker & Docker Compose (optional, but recommended for containerized setup)

---

## 🚀 Getting Started

### 1. Train the Model
Before running the API, you must train and save the machine learning model.
The training script will generate the `model.joblib` artifact inside the `app/` directory.

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the training script
python train.py
```
*Expected Output:* `Model trained and saved to app/model.joblib`

---

### 2. Run the Application

You can run the API locally using standard Python/Uvicorn or via Docker.

#### Option A: Run Locally (Uvicorn)
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at: http://localhost:8000

#### Option B: Run via Docker Compose
Make sure the `model.joblib` artifact was created before building the image.
```bash
# Build and start the container in detached mode
docker-compose up -d --build
```
The API will be available at: http://localhost:8000

---

## 📖 API Documentation

Once the application is running, you can access the interactive API documentation provided by FastAPI:
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoints

#### 1. Health Check
Checks if the API is running and if the model is successfully loaded.
- **URL:** `/health`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "status": "healthy",
    "service": "model-serving",
    "model_loaded": true
  }
  ```

#### 2. Predict
Generates a house price prediction based on square footage and number of bedrooms.
- **URL:** `/predict`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "square_footage": 1200.0,
    "bedrooms": 2
  }
  ```
- **Response:**
  ```json
  {
    "predicted_value": 160000.0,
    "model_version": "v0.2-scikit"
  }
  ```

---

## 🧪 Running Tests

The project includes test cases using `pytest` to verify the health check and prediction endpoints.

To run the tests:
```bash
pytest tests/
```

---


