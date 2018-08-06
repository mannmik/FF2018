from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserAccount
import json




def LogIn(request):
    if request.method == 'POST':
        data = request.POST.copy()
        user = auth.authenticate(username=data['username'], password=data['password'])
        #TODO dont remember username?

        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return render (request, 'login.html', {'error':'Username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        return redirect('home')


def SignUp(request):
    # new account
    if request.method == 'POST':
        data = request.POST.copy()
        # check if the user email or username already exists
        if data['password'] == data['passwordConfirm']:
            try:
                if User.objects.get(email = data['email'].lower()):
                    return render(request, 'signup.html', {'error':'Sorry, that email already exists.'} )
                elif User.objects.get(username = data['username'].lower()):
                    return render(request, 'signup.html', {"error":"Sorry, " + data['username'] + " already exists."} )
            except User.DoesNotExist:
                usr = User.objects.create_user(data['username'], email=data['email'], password=data['password'])
                auth.login(request, usr)
                return render(request, 'home.html')
        else:
            return render(request, 'signup.html', {"error":"Passwords do not match."})
    else:
        return render(request, 'signup.html')