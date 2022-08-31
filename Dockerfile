FROM python:3.8-slim-buster

RUN apt-get update -y && apt-get install -y gcc
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


COPY . .