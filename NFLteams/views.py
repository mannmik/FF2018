from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from FF2018 import api_services
from . models import NFL_Team
from bs4 import BeautifulSoup
from Player import web_scraper
from collections import namedtuple
from NFLteams import services
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
        # clear out any old data before initializing with new data
        services.delete_all_NFL_Teams()

        # use api_services to call FFN API to get the team name info
        # json list is returned
        teams = api_services.get_nfl_teams()

        # use api_services to get the nfl team bye weeks
        # json list is returned
        byes = api_services.get_byeweeks()

        # stores the team codes for each NFL team
        teamList = []
    
        # create new team objects from list of NFL objects 
        # returned from the API
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

        # fill in the teams' strength of schedules for regular season and playoffs
        services.set_strength_of_schedule()

        # set up the teams' playoff schedule
        services.set_playoff_schedule()

        return render(request, 'teams.html', {"teamList":teamList} )
    else:
        return render(request, 'login.html' , {"error": "You must be logged in to complete this action."})


def Teams(request):
    team_list = NFL_Team.objects
    return render(request, 'teams.html', {"team_list":team_list})

def SOS(request):
    # services.set_playoff_schedule()
    #sos = web_scraper.strength_of_schedule_scraper()
    # teams = []
    # teams.append({"Team":"BUF", "QB":1, "RB":10, "WR":17})
    # teams.append({"Team":"ARI", "QB":2, "RB":6, "WR":20})
    # teams.append({"Team":"JAX", "QB":3, "RB":27, "WR":4})
    # teams.append({"Team":"PHI", "QB":4, "RB":12, "WR":19})
    # teams.append({"Team":"NO", "QB":5, "RB":19, "WR":16})
    # teams.append({"Team":"LAC", "QB":6, "RB":14, "WR":14})
    # teams.append({"Team":"DEN", "QB":7, "RB":5, "WR":23})
    # teams.append({"Team":"DAL", "QB":8, "RB":23, "WR":12})
    # teams.append({"Team":"PIT", "QB":9, "RB":21, "WR":11})
    # teams.append({"Team":"MIN", "QB":10, "RB":13, "WR":7})
    # teams.append({"Team":"BAL", "QB":11, "RB":11, "WR":26})
    # teams.append({"Team":"CHI", "QB":12, "RB":3, "WR":25})
    # teams.append({"Team":"NYG", "QB":13, "RB":31, "WR":9})
    # teams.append({"Team":"OAK", "QB":14, "RB":29, "WR":2})
    # teams.append({"Team":"ATL", "QB":15, "RB":16, "WR":3})
    # teams.append({"Team":"TEN", "QB":16, "RB":17, "WR":15})
    # teams.append({"Team":"SF", "QB":17, "RB":24, "WR":18})
    # teams.append({"Team":"TB", "QB":18, "RB":20, "WR":8})
    # teams.append({"Team":"KC", "QB":19, "RB":15, "WR":30})
    # teams.append({"Team":"CAR", "QB":20, "RB":22, "WR":1})
    # teams.append({"Team":"MIA", "QB":21, "RB":8, "WR":5})
    # teams.append({"Team":"LAR", "QB":22, "RB":30, "WR":6})
    # teams.append({"Team":"GB", "QB":23, "RB":32, "WR":10})
    # teams.append({"Team":"WAS", "QB":24, "RB":28, "WR":29})
    # teams.append({"Team":"NYJ", "QB":25, "RB":26, "WR":27})
    # teams.append({"Team":"HOU", "QB":26, "RB":4, "WR":28})
    # teams.append({"Team":"DET", "QB":27, "RB":2, "WR":13})
    # teams.append({"Team":"NE", "QB":28, "RB":1, "WR":32})
    # teams.append({"Team":"SEA", "QB":29, "RB":18, "WR":24})
    # teams.append({"Team":"CLE", "QB":30, "RB":9, "WR":22})
    # teams.append({"Team":"CIN", "QB":31, "RB":25, "WR":21})
    # teams.append({"Team":"IND", "QB":32, "RB":7, "WR":31})

    return render(request, 'success.html', {"news": NFL_Team.objects})


    