# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set the working directory in the Docker image
WORKDIR /usr/src

# Copy the current directory contents into the container at /usr/src/app
COPY app /usr/src/app

# Copy the requirements.txt file into the container at /usr/src/app
COPY app/requirements.txt /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.main when the container launches
CMD ["python", "-m", "app.main"]
