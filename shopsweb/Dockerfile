FROM python:3.6

LABEL maintainer="khaliayoub9@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./ ./app

WORKDIR ./app

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir logs

ENV FLASK_APP=run.py

CMD ["uwsgi", "shops_app.ini"]