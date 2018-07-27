from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from FF2018 import api_services
from . models import NFL_Team
from bs4 import BeautifulSoup
from collections import namedtuple
import requests
import json


'''
This will be the initial team set up and should only be run once before each season.
Updates all the nfl team codes, fullNames, and shortNames
Updates the bye weeks for each nfl team

Calls the Fantasy Football Nerds API for the team's info

'''
def Init(request):
    if request.user.is_staff:

        # use api_services to call FFN API to get the team name info
        # json list is returned
        teams = api_services.get_nfl_teams()

        # use api_services to get the nfl team bye weeks
        # json list is returned
        byes = api_services.get_byeweeks()

        # stores the team codes for each NFL team
        teamList = []

        for i in teams["NFLTeams"]:
            newTeam = NFL_Team()
            newTeam.code = i['code']
            newTeam.fullName = i['fullName']
            newTeam.shortName = i['shortName']
            
            for j in byes:
                for k in byes[j]:
                    if k['team'] == i['code']:
                        newTeam.byeWeek = k["byeWeek"]
                    else:
                        continue

            teamList.append(newTeam)

        return render(request, 'success.html', {"teamList":teamList} )
    else:
        return redirect('home')


def CheatSheet(request):
   
    playerList = api_services.cheat_sheet_scraper("QB")
    rb_list = api_services.cheat_sheet_scraper("RB")
    #link = api_services.cheat_sheet_scraper()
    return render(request, 'success.html', {"link":playerList, "rb":rb_list})
    