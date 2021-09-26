# base image
FROM python:3.8 
# setup environment variables
ENV DockerHOME=/home/app/webapp
ENV DjangoPROJECT=dj_docker_drf
ENV CustomPort=8888

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
# copy whole project to your docker home directory
COPY . $DockerHOME
# run this command to install all dependencies
RUN pip install -r requirements.txt
# start server
EXPOSE $CustomPort
CMD cd $DjangoPROJECT && \
 python manage.py makemigrations && \
 python manage.py migrate && \
 python manage.py runserver 0.0.0.0:$CustomPort