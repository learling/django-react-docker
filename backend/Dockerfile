FROM python:3.8

LABEL maintainer="dev@ivanne.de"

ENV DockerHOME=/home/app/webapp
ENV DjangoPROJECT=dj_docker_drf

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHOME

RUN pip install -r requirements.txt
# start development server
#CMD cd $DjangoPROJECT && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000