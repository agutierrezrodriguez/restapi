FROM python:2.7

MAINTAINER "Antonio Gutiérrez <toniusco@gmail.com>"

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app/

CMD [ "gunicorn", "-c", "/app/gunicorn_config.py", "--log-file", "-", "restapi.wsgi" ]