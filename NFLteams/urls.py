from django.urls import path, include
from . import views


urlpatterns = [
    path('init', views.Init, name="init"),
    path('', views.Teams, name="nflteams"),
    #path('cheatsheet', views.CheatSheet, name="cheatsheet"),
    #path('signup/', views.SignUp, name="signup"),
    #path('logout/', views.logout, name="logout"),
]