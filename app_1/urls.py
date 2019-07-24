from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('slide' , views.slide, name='slide'),
]