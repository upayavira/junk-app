FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python-pip && \
    pip install --upgrade pip && \
    pip install Flask && \
    mkdir /app

ADD . /app
WORKDIR /app
CMD python app.py
