FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

RUN apt-get update && apt-get -y install curl

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app
COPY poetry.lock pyproject.toml ./

# RUN poetry install --no-dev
RUN pip install httpx

RUN pip install opentelemetry-api

RUN pip install opentelemetry-sdk

RUN pip install opentelemetry-instrumentation-fastapi

RUN pip install opentelemetry-instrumentation-logging

RUN pip install opentelemetry-instrumentation-sqlalchemy

RUN pip install opentelemetry-exporter-otlp

RUN pip install loguru

COPY python_tracing_demo/ ./

ENV PORT=8080