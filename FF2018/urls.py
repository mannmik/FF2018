
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    #path('login/', views.LogIn),
    path('useraccount/', include('UserAccount.urls')),
]
