# Use an official Python runtime as a parent image
FROM python:3.11.7

# Set the working directory in the Docker image
WORKDIR /usr/src/app

# Copy the requirements.txt first to leverage Docker cache
COPY app/requirements/requirements.txt /usr/src/app/requirements/
RUN pip install --no-cache-dir -r requirements/requirements.txt

# Copy the app directory contents into the container at /usr/src/app
COPY app/ /usr/src/app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Install curl for health check
RUN apt-get update && apt-get install -y curl

HEALTHCHECK --interval=5m --timeout=3s \
  --start-period=1m \
  CMD curl --fail http://localhost:8000/docs || exit 1

# Run main.py when the container launches
CMD ["python", "main.py", "--host", "127.0.0.1", "--port", "8000"]

ENV APP_MODULE=main
