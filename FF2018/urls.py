
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('fantasyfootball/admin/', admin.site.urls),
    path('fantasyfootball', views.Home, name='home'),
    #path('login/', views.LogIn),
    path('fantasyfootball/useraccount/', include('UserAccount.urls')),
    path('fantasyfootball/nflteams/', include('NFLteams.urls')),
    path('fantasyfootball/player/', include('Player.urls')),
]
