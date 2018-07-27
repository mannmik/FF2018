import json
import requests
from django.shortcuts import render, redirect

'''
This file will handle our api services 

'''

def get_nfl_teams():
    # need the url of ffn we are going to
    url = "https://www.fantasyfootballnerd.com/service/nfl-teams/json/test/"

    # set up our parameters
    # r = requests.get(url, params=params)
    req = requests.get(url)

    # load the request
    data = req.json()#json.loads(req.content)
    
    # load json 
    # to dict?
    # retrun the dict
    return data
