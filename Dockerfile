FROM python:3.8

COPY Pipfile.lock Pipfile app.py /app/
WORKDIR /app
RUN pip install pipenv ; pipenv sync --system
EXPOSE 5000
CMD flask run --host=0.0.0.0
