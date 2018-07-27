from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Update, name="update"),
    #path('signup/', views.SignUp, name="signup"),
    #path('logout/', views.logout, name="logout"),
]