from django.http import HttpResponse
from django.shortcuts import render
from Player import web_scraper


def Home(request):

    # ----------- TODO -------------
    # Web scrape player news for the player news tab
    player_news = web_scraper.fantasy_news_scraper()
    # Web scrape from multiple sites
    # --------------------------------
    return render(request,'home.html', {"news":player_news})

#def LogIn(request):
    #return render(request, 'userAccounts/login.html')
