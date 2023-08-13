# app/Dockerfile

FROM python:3.11.4-slim
LABEL authors="johndutchover"

WORKDIR /app
ENV PYTHONPATH /app

RUN mkdir /app/.streamlit
RUN mkdir /app/pages

COPY .env /app
COPY .streamlit/secrets.toml /app/.streamlit
COPY . .
EXPOSE 8501
ENTRYPOINT ["sh", "/app/start_streamlit.sh"]
