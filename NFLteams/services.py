from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from FF2018 import api_services
from . models import NFL_Team
from bs4 import BeautifulSoup
from Player import web_scraper
from collections import namedtuple
import requests
import json
import pandas as pd 

'''
Deletes all of the NFL_Team objects
'''
def delete_all_NFL_Teams():
    NFL_Team.objects.all().delete()

'''
Function sets the strength of schedule by position for every
NFL team. Sets a regular season SOS for weeks 1-6 and
sets a playoff sos for weeks 14-16.
Uses panadas to read sos info from excel sheets and 
stores them in our NFL-team objects.
'''
def set_strength_of_schedule():

    # get all team objects
    teams = NFL_Team.objects

    # open wk 1-16 sos
    reg_season = pd.read_excel('wk_1-16_SOS_2018.xlsx')

    # open / read wk 14-16 sos
    playoffs  = pd.read_excel('wk_14-16_SOS_2018.xlsx')

    # regular season sos 
    # loop through range of all teams in the TEAM column of the excel sheet
    for i in range(len(reg_season['TEAM'])):

        # get the team name at row i in the TEAM column
        teamCode = NFL_Team.objects.get(code = reg_season.loc[i, "TEAM"])

        # get the nfl team object that matches that unique team code
        team = NFL_Team.objects.get(code = teamCode)

        # update the sos for each position
        team.qb_SOS = reg_season.loc[i, 'QB']
        team.rb_SOS = reg_season.loc[i, 'RB']
        team.wr_SOS = reg_season.loc[i, 'WR']
        team.te_SOS = reg_season.loc[i, 'TE']

        # save/update the current nfl team object
        team.save()
    
    # playoff sos
    # loop through range of all teams in the TEAM column of the excel sheet
    for i in range(len(playoffs['TEAM'])):

        # get the team name at row i in the TEAM column
        teamCode = NFL_Team.objects.get(code = playoffs.loc[i, "TEAM"])

        # get the nfl team object that matches that unique team code
        team = NFL_Team.objects.get(code = teamCode)

        # update the sos for each position
        team.qb_Playoff = playoffs.loc[i, 'QB']
        team.rb_Playoff = playoffs.loc[i, 'RB']
        team.wr_Playoff = playoffs.loc[i, 'WR']
        team.te_Playoff = playoffs.loc[i, 'TE']

        # save/update the current nfl team object
        team.save()


'''
Function sets each NFL_Team objects' playoff schedule
Schedule is for weeks 13-16
Reads information from the wk_13-16 excel sheet
'''
def set_playoff_schedule():
    teams = NFL_Team.objects.order_by('code')

    schedule = pd.read_excel('wk_13-16_schedule.xlsx')

    for i in range(len(teams)):
        teams[i].wk13 = schedule.loc[i, 'wk13']
        teams[i].wk14 = schedule.loc[i, 'wk14']
        teams[i].wk15 = schedule.loc[i, 'wk15']
        teams[i].wk16 = schedule.loc[i, 'wk16']

        teams[i].save()
