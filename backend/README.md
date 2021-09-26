# Getting started with Django

```
pip install virtualenv
virtualenv .
pip install django
```

## https://blog.logrocket.com/dockerizing-a-django-app/

```
django-admin startproject dj_docker_drf
cd dj_docker_drf
django-admin startapp sample
cd ..
pip install djangorestframework
pip freeze > requirements.txt
docker build . -t docker-django-v0.0
docker run -p 127.0.0.1:8888:8000/tcp docker-django-v0.0
```

## Compose

```
cd ..
docker-compose up db web proxy
```

## Static files

`backend/dj_docker_drf/build/static` and `backend/dj_docker_drf/build/index.html` are needed.

https://medium.com/codex/deploying-react-through-djangos-static-files-part-1-dev-setup-8a3a7b93c809