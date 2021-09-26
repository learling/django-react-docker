"""dj_docker_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from sample.views import SampleView
from django.shortcuts import render

def render_react(request):
    return render(request, "index.html")

urlpatterns = [
    path('api/', SampleView.as_view()),
    re_path(r'^$', render_react),
    re_path(r'^(?:.*)/?$', render_react),
]