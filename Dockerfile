# Use an official Python runtime as a parent image
FROM python:3.11.4

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

# Set the working directory in the Docker image
WORKDIR /usr/src/app

# Copy the requirements.txt first to leverage Docker cache
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory contents into the container at /usr/src/app
COPY app/ .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.main when the container launches
CMD ["python", "-m", "main"]
