from django.urls import path, include
from . import views


urlpatterns = [
    path('init', views.Init, name="init"),
    path('', views.Teams, name="nflteams"),
   
]