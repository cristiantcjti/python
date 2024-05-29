FROM python:3.11.0-slim

ENV PYTHONUNBUFFERED 1

ENV FLASK_APP=/app/wsgi.py

ARG APP_HOME=/app/

RUN apt update \
  && apt install -y libpq-dev gcc

RUN pip install --upgrade pip pipenv

WORKDIR ${APP_HOME}

COPY Pipfile $APP_HOME

COPY Pipfile.lock $APP_HOME

RUN pipenv install --system --deploy

COPY src ${APP_HOME}

CMD /bin/sh -c "flask db upgrade; gunicorn --config gunicorn_conf.py wsgi:app --reload"
