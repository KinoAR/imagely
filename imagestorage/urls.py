# URL configuration - paths for the application

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index')
]