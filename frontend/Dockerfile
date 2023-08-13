# app/Dockerfile

FROM python:3.11.4-slim-bookworm
LABEL authors="johndutchover"

WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Combine mkdir commands and create necessary directories
RUN mkdir -p /app/.streamlit /app/pages

# Copy only the requirements file and install dependencies
COPY fe-requirements.txt /app/fe-requirements.txt
RUN pip install --no-cache-dir -r fe-requirements.txt

# Copy the specific files and directories you need
COPY .env /app
COPY .streamlit/secrets.toml /app/.streamlit
COPY pages /app/pages
COPY start_streamlit.sh /app/start_streamlit.sh

EXPOSE 8501
ENTRYPOINT ["bash", "/app/start_streamlit.sh"]
