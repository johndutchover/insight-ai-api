# Use an official Python runtime as a parent image
FROM python:3.11.6-slim-bookworm

# Set the working directory in the Docker image
WORKDIR /client
ENV PYTHONPATH /client

# Copy the requirements.txt first to leverage Docker cache
COPY requirements/requirements-frontend.txt /client/requirements-frontend.txt
COPY frontend/start_streamlit.sh /client/start_streamlit.sh

RUN chmod +x /client/start_streamlit.sh
RUN pip install --no-cache-dir -r requirements-frontend.txt

# Copy the app directory contents into the container at /client/frontend
COPY frontend/ .

# Make port 8501 available to the world outside this container
EXPOSE 8501

HEALTHCHECK --interval=5m --timeout=3s \
  --start-period=1m \
  CMD curl --fail http://localhost:8501 || exit 1


# Run startup script
ENTRYPOINT ["bash", "start_streamlit.sh"]
