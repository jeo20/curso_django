from django.urls import include, path

from . import views

urlpatterns = [
    path('create/', views.create, name="create")
]