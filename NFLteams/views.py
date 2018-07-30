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

        # ----------- TODO ----------
        # Need to web scrape the strength of schedule 
        # scrape weeks 10-16 for each time
        # FF toolbox has info all in one place
        # then add all of these attributes to our new NFL_Team object in the loop
        #----------------------------

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
            newTeam.save()

        return render(request, 'teams.html', {"teamList":teamList} )
    else:
        return render(request, 'login.html' , {"error": "You must be logged in to complete this action."})


def Teams(request):
    team_list = NFL_Team.objects
    return render(request, 'teams.html', {"team_list":team_list})


# def CheatSheet(request):
   
#     qb_list = api_services.cheat_sheet_scraper("QB")
#     rb_list = api_services.cheat_sheet_scraper("RB")
#     wr_list = api_services.cheat_sheet_scraper("WR")
#     te_list = api_services.cheat_sheet_scraper("TE")
    
#     players = []

#     PlayerTable = namedtuple("PlayerTable", "qb_name qb_link rb_name rb_link wr_name wr_link te_name te_link")

#     for i in range(len(rb_list)):
#         if i <= 36:
#             players.append(PlayerTable(qb_list[i][0], qb_list[i][1], rb_list[i][0], rb_list[i][1], wr_list[i][0], wr_list[i][0], te_list[i][0], te_list[i][1] ))
#         else:
#             players.append(PlayerTable("", "", rb_list[i][0], rb_list[i][1], wr_list[i][0], wr_list[i][0], "", "" ))

#     #link = api_services.cheat_sheet_scraper()
#     return render(request, 'success.html', {'players':players})
    