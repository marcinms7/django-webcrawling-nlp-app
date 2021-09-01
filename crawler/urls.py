from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from crawler import views

app_name = 'crawler'

urlpatterns = [
path('', views.crawler, name='crawler'),
# path('', views.index, name='index')
]