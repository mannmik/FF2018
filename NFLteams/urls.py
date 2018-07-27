from django.urls import path, include
from . import views

urlpatterns = [
    path('init', views.Init, name="init"),
    path('cheatsheet', views.CheatSheet, name="cheatsheet"),
    #path('signup/', views.SignUp, name="signup"),
    #path('logout/', views.logout, name="logout"),
]