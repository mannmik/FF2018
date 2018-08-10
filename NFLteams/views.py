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




    