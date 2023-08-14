FROM python:3.11.4-slim-bookworm
WORKDIR /client
ENV PYTHONPATH "${PYTHONPATH}:/client"

COPY .env /client
RUN mkdir -p /client/.streamlit
COPY .streamlit/secrets.toml /client/.streamlit/
COPY fe-requirements.txt /client/fe-requirements.txt
RUN pip install --no-cache-dir -r fe-requirements.txt
COPY . /client
EXPOSE 8501
ENTRYPOINT ["bash", "/client/start_streamlit.sh"]
