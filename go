#!/bin/sh

docker build -t docker.odoko.org/app:latest .
docker push docker.odoko.org/app:latest
