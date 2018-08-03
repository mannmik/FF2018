from django.urls import path, include
from . import views

urlpatterns = [
    path('cheatsheet', views.CheatSheet, name="cheatsheet"),
    path('news', views.PlayerNews, name="playernews"),
    path('init', views.Player_Init, name="playerinit"),
]