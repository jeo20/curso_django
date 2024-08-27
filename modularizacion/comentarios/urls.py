# Copio el contenido del archivo urls.py del proyecto modularizacion
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test, name='test'), #  url test
    path('create/', views.create, name='create'), #  url create
    path('delete/', views.delete, name = 'delete') #  url delete
]