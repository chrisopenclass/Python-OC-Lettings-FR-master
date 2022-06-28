# syntax=docker/dockerfile:1

# Image used
FROM python:3.10-slim-buster

# default path
WORKDIR /oc_lettings

ENV PYTHONDONTWRITEBYTECODE=1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED=1
#port number
ENV PORT=8000

COPY requirements.txt /oc_lettings_site

# install dependencies
RUN pip install -r requirements.txt

# Adding source code to the image
COPY . .

# Expose an external port
EXPOSE $PORT

# Run django server
CMD python manage.py runserver 0.0.0.0:$PORT