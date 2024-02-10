# Use an official Python runtime as a parent image
FROM python:3.11.7

# Set the working directory in the Docker image
WORKDIR /usr/src/app

# Create the requirements directory
RUN mkdir requirements

# Copy requirements.txt into the container at /usr/src/app/requirements/
COPY requirements/requirements.txt requirements/

# Install dependencies
RUN pip install --no-cache-dir -r requirements/requirements.txt

# Copy the .env file into the container at /usr/src/app
COPY .env .
# Copy the rest of the app directory contents into the container at /usr/src/app
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Install curl for health check
RUN apt-get update && apt-get install -y curl

HEALTHCHECK --interval=5m --timeout=3s \
  --start-period=1m \
  CMD curl --fail http://localhost:8000/docs || exit 1

# Run main.py when the container launches
CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "8000"]

ENV APP_MODULE=main
ENV MARVIN_OPENAI_CHAT_COMPLETIONS_MODEL=gpt-3.5-turbo
