FROM python:3.7-alpine

COPY Pipfile.lock Pipfile app.py /app/
WORKDIR /app
RUN apk add --no-cache git build-base libxml2-dev libxslt-dev; pip install pipenv ; pipenv sync
CMD pipenv run flask
