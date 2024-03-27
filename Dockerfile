# syntax=docker/dockerfile:1
# Use an official Python runtime as a parent image
FROM python:3.11 as base

# Set the working directory in the Docker image
WORKDIR /app

# Create and activate a virtual environment
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Copy requirements.txt and install dependencies
COPY app/requirements/requirements.txt /app/requirements.txt
RUN /app/venv/bin/pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the app directory into the container at /app
COPY app/ /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Install curl for health check
RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

HEALTHCHECK --interval=5m --timeout=3s \
  --start-period=1m \
  CMD curl --fail http://localhost:8000/docs || exit 1

# Set entrypoint for FastAPI when the container launches
CMD ["/app/venv/bin/python", "main.py"]
