# syntax=docker/dockerfile:1
# Use an official Python runtime as a parent image
FROM python:3.11.7 as base

# Set the working directory in the Docker image
WORKDIR /usr/src/app

# Copy the entire app directory into the container at /usr/src/app
COPY app/requirements/requirements.txt /usr/src/app
# use trailing . to include hidden files
COPY app/. /usr/src/app

# Create and activate a virtual environment
RUN python -m venv venv

# Activate the virtual environment and install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Install curl for health check
RUN apt-get update && apt-get install --no-install-recommends -y curl=8.5.0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

HEALTHCHECK --interval=5m --timeout=3s \
  --start-period=1m \
  CMD curl --fail http://localhost:8000/docs || exit 1

# Set entrypoint for FastAPI when the container launches
ENTRYPOINT ["python", "main.py"]
