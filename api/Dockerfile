# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Run the server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
