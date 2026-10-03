# 1. Base Linux image with Python pre-installed
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the application code
COPY app/ ./app

# 6. Expose the port the app listens on
EXPOSE 8000

# 7. Start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]