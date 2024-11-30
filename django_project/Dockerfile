# Base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    && apt-get clean

# Set work directory
WORKDIR /app

# Copy dependencies file first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
