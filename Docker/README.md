# Python Hello World in Docker on Google Cloud Platform (GCP)

This project demonstrates how to deploy a simple Python "Hello World" script in a Docker container on Google Cloud Platform (GCP). The repository provides all the necessary files and instructions to build, test, and deploy the Docker container using Google Cloud Run.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your local machine
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed and configured
- A Google Cloud Platform (GCP) account with a project set up

## Project Structure
```
/Docker
│
├── app.py # Python script that prints "Hello World"
├── Dockerfile # Dockerfile to containerize the Python script
├── requirements.txt # Python dependencies
└── README.md # This documentation file
```
## Step-by-Step Guide

### 1. Prepare the Python Script

The Python script (`app.py`) simply prints "Hello World" to the console:

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```
### 2. Create the Dockerfile
```
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY app.py .

# Run the Flask application when the container launches
CMD ["python", "app.py"]
```
### 3. Build the Docker Image
```
docker build -t my-python-app .
```

### 4. Test the Docker Image Locally
```
docker run -p 8080:8080 my-python-app
```
Visit http://localhost:8080 in your browser. You should see "Hello World".

### 4. Deploy to Google Cloud Platform (GCP)

a. Set up Google Cloud SDK and GCP Project
Log in to Google Cloud and set your project:

```
gcloud auth login
gcloud config set project [YOUR_PROJECT_ID]
```

b. Enable Google Cloud Run
Enable the Cloud Run service in your project:

```
gcloud services enable run.googleapis.com
```
c. Push Docker Image to Google Container Registry
Tag and push your Docker image to Google Container Registry (GCR):
```
docker tag my-python-app gcr.io/[YOUR_PROJECT_ID]/python-hello-world
docker push gcr.io/[YOUR_PROJECT_ID]/python-hello-world
```
d. Deploy Docker Image to Google Cloud Run
Deploy the Docker image to Google Cloud Run:

```
gcloud run deploy python-hello-world --image gcr.io/[YOUR_PROJECT_ID]/python-hello-world --platform managed --region europe-west1
```
Select y to allow unauthenticated invocations.
Note the URL provided by the command; this is where your service is running.

### 6. Access Your Deployed Service
Visit the URL provided by Cloud Run to see the output of your Python script. You should see "Hello World" displayed.
