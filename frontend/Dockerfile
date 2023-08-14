FROM python:3.11.4-slim-bookworm
WORKDIR /client
ENV PYTHONPATH /client

COPY fe-requirements.txt /client/fe-requirements.txt
COPY start_streamlit.sh /client/start_streamlit.sh
RUN chmod +x /client/start_streamlit.sh
RUN pip install --no-cache-dir -r fe-requirements.txt
COPY . .
EXPOSE 8501
ENTRYPOINT ["bash", "/client/start_streamlit.sh"]
