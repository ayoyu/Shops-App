FROM python:3.6

LABEL maintainer="khaliayoub9@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./ ./app

WORKDIR ./app

RUN pip install --no-cache-dir -r requirements.txt

# create logs directory for uwsgi logs & docker volume 
RUN mkdir logs

# set FLASK_APP for creating tables with SQLAlchemy
ENV FLASK_APP=run.py

CMD ["uwsgi", "shops_app.ini"]