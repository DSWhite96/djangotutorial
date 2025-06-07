#This file is used to map the views to URL configurations (URLconf)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]