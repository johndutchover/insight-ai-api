FROM python:3.11.4-slim-bookworm
WORKDIR /client
ENV PYTHONPATH /client

COPY frontend/requirements_frontend.txt /client/requirements_frontend.txt
COPY frontend/start_streamlit.sh /client/start_streamlit.sh
RUN chmod +x /client/start_streamlit.sh
RUN pip install --no-cache-dir -r requirements_frontend.txt
COPY frontend/ .
EXPOSE 8501
ENTRYPOINT ["bash", "start_streamlit.sh"]
