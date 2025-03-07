FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libc6-dev \
    libmupdf-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app

EXPOSE 8000

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000