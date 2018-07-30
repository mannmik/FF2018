from django.urls import path, include
from . import views

urlpatterns = [
    path('cheatsheet', views.CheatSheet, name="cheatsheet"),
]