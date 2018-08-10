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
   
    baseUrl = "https://www.fantasyfootballnerd.com/service/nfl-teams/"  # need the url of ffn and the API service we want
    key = "e9zs2aed4rjm"                                                # the api key for our free account created for this site
    dataType = "json/"                                                  # tells the API that we want data in json format not xml
    url = baseUrl + dataType + key                                      # combining all of our parameters to create the full URL for our API calls
    
    # make our call to the API
    req = requests.get(url)

    # gather json data from our request
    data = req.json()
    
    return data


'''
Gathers the teams on a bye in each bye week.
API call returns each bye week with team, byeWeek, and displayName attributes
These attributes are present for each NFL team on a by that week

'''
def get_byeweeks():
    baseUrl = "https://www.fantasyfootballnerd.com/service/byes/"   # need the base url of ffn and the API service we want
    key = "e9zs2aed4rjm"                                            # the api key for our free account created for this site
    dataType = "json/"                                              # tells the API that we want data in json format not xml
    url = baseUrl + dataType + key                                  # combining all of our parameters to create the full URL for our API calls

    req = requests.get(url)

    data = req.json()

    return data


