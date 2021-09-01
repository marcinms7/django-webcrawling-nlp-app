from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from api import views
# Create your views here.

app_name = 'api'

urlpatterns = [
path('', views.api, name='api'),
# path('', views.index, name='index')
]