# Base image
FROM python:3.9-slim

# Set environment variable for port
ENV PORT 8080

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . /app
WORKDIR /app

# Expose the port that the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]