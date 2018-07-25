from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserAccount


def LogIn(request):
    if request.method == 'POST':
        if request.POST['email']:
            usr = UserAccount.objects.get(usrEmail = request.POST['email'])
            return render(request, 'success.html')
    else:
        return render(request, 'login.html')
