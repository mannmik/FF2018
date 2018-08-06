import json
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from collections import namedtuple

'''
This file will handle our api services.
We make calls to Fantasy Football Nerd's API following their specified documentation.

'''

'''
Gathers information for all NFL teams.
API call returns code, fullName and shortName of each NFL Team 

'''
def get_nfl_teams():
    # need the url of ffn we are going to
    baseUrl = "https://www.fantasyfootballnerd.com/service/nfl-teams/"
    key = "e9zs2aed4rjm"
    dataType = "json/"
    url = baseUrl + dataType + key
    
    # set up our parameters
    # r = requests.get(url, params=params)
    req = requests.get(url)

    # load the request
    data = req.json() #json.loads(req.content)
    
    return data


'''
Gathers the teams on a bye in each bye week.
API call returns each bye week with team, byeWeek, and displayName attributes
These attributes are present for each NFL team on a by that week

'''
def get_byeweeks():
    baseUrl = "https://www.fantasyfootballnerd.com/service/byes/"
    key = "e9zs2aed4rjm"
    dataType = "json/"
    url = baseUrl + dataType + key

    req = requests.get(url)

    data = req.json()

    return data


