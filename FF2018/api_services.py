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
    url = "https://www.fantasyfootballnerd.com/service/nfl-teams/json/test/"

    # set up our parameters
    # r = requests.get(url, params=params)
    req = requests.get(url)

    # load the request
    data = req.json() #json.loads(req.content)
    
    # load json 
    # to dict?
    # retrun the dict
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


def cheat_sheet_scraper():
    baseUrl = "https://www.fantasypros.com"
    cht_sht = "/nfl/cheatsheets/"

    req = requests.get(baseUrl + cht_sht)
    soup = BeautifulSoup(req.content)

    PlayerStruct = namedtuple("PlayerStruct", "Name Link")
    playerList = []

    qb_data = soup.find_all("div", {"class":"three columns position-QB"})
    for i in qb_data:
        print(i.contents[1])

    qb_name = qb_data[0].contents[3].find_all("a")  
    qb_team = qb_data[0].contents[3].find_all("small", {"class":"grey"})
    qb_link = qb_data[0].contents[3].find_all("a")

    # for qb in qb_name:
    #     print(qb.text)

    # for team in qb_team:
    #     print(team.text)

    for link in qb_link:
        baseUrl = "https://www.fantasypros.com"
        player = PlayerStruct(link.text, baseUrl + link.get('href'))
        playerList.append(player)
        # url = baseUrl + link.get('href')
        # print(url)
    
    #theUrl = baseUrl + qb_link[0].get('href')
    return playerList