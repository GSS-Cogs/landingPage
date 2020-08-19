FROM python:3.7

COPY Pipfile.lock Pipfile app.py /app/
WORKDIR /app
RUN pip install pipenv ; pipenv install --system
EXPOSE 5000
CMD flask run --host=0.0.0.0
