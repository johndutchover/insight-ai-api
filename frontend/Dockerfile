# app/Dockerfile

FROM python:3.11.4-slim-bookworm
LABEL authors="johndutchover"

WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Copy only the requirements file and install dependencies
COPY fe-requirements.txt /app/fe-requirements.txt
RUN pip install --no-cache-dir -r fe-requirements.txt

# Copy all files and directories from the current directory to /app
COPY . /app

EXPOSE 8501
ENTRYPOINT ["bash", "/app/start_streamlit.sh"]
