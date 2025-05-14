FROM --platform=linux/amd64 python:3.11-buster as build


WORKDIR /app

COPY requirements.txt .
COPY .env .


RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python run.py"]