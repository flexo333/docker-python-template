# BASIC INSTALL
FROM python:3-buster
RUN apt-get update -qq

RUN mkdir /app
WORKDIR /app
COPY ./app /app