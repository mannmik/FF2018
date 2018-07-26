
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LogIn, name="login"),
    path('signup/', views.SignUp, name="signup"),
    path('logout/', views.logout, name="logout"),
]
