from django.http import HttpResponse
from django.shortcuts import render


def Home(request):

    # ----------- TODO -------------
    # Web scrape player news for the player news tab
    # Web scrape from multiple sites
    # --------------------------------
    return render(request,'home.html')

#def LogIn(request):
    #return render(request, 'userAccounts/login.html')
