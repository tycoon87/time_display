from django.conf.urls import url
from apps.time_app import views

url(r'^$', views.index, name='index')
