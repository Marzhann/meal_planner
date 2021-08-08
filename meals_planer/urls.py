"""Defines URL patterns for meals_planer"""

from django.urls import path
from . import views

app_name = 'meals_planer'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]