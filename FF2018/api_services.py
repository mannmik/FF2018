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


def cheat_sheet_scraper(pos):

    # struct used to store this info temorarily
    # TODO save in a Player app / model
    PlayerStruct = namedtuple("PlayerStruct", "Name Link")

    # empty player list that will be returned
    qb_list = scrape_player(pos)

    return qb_list
    


    # # the base url info we are using to scrape the cheatsheet
    # baseUrl = "https://www.fantasypros.com"
    # cht_sht = "/nfl/cheatsheets/"

    # # we make a get request to fantasy webpage and store the content
    # req = requests.get(baseUrl + cht_sht)

    # # store the content for scraping
    # soup = BeautifulSoup(req.content)

    # # struct used to store this info temorarily
    # # TODO save in a Player app / model
    # PlayerStruct = namedtuple("PlayerStruct", "Name Link")

    # # empty player list that will be returned
    # playerList = []
   
    # '''
    # These scrape fantasy pros for the data of the player in a certain column of the cheat sheet.
    # We scrape the name and team code of the player and then the link to the player profile

    # '''
    # qb_data = soup.find_all("div", {"class":"three columns position-QB"})               # grabs the whole ranking list for that position
    # qb_name = qb_data[0].contents[3].find_all("a")                                      # grabs the name
    # qb_team = qb_data[0].contents[3].find_all("small", {"class":"grey"})                # grabs the team code i.e. "SF"
    # qb_link = qb_data[0].contents[3].find_all("a")                                      # grabs all the link to player profiles

    # # tracks the actual player links
    # # each player has two <a> tags but one is empty
    # totalValidLinks = 0

    # # for loop fills our player struct with the required info
    # # loops through the length of the players scraped
    # for i in range(len(qb_name)):
    #     # holds the href link for the player to fantasypros site
    #     link = qb_link[i].get('href')

    #     # if this is one of the valid links
    #     if link != "#":
    #         # save the text of our player
    #         name = qb_name[i].text + ", " + qb_team[totalValidLinks].text

    #         # increase the valid links found
    #         totalValidLinks += 1

    #         # store the iinformation gathered in our player structs
    #         player = PlayerStruct(name, baseUrl + link)

    #         # add to our list of players
    #         playerList.append(player)

    # # for link in qb_link:
    # #     lnk = link.get('href')
    # #     if lnk != "#":
    # #         player = PlayerStruct(link.text, baseUrl + link.get('href'))
    # #         playerList.append(player)
    
    # # return our list of players
    


def scrape_player(position):

     # the base url info we are using to scrape the cheatsheet
    baseUrl = "https://www.fantasypros.com"
    cht_sht = "/nfl/cheatsheets/"

    # we make a get request to fantasy webpage and store the content
    req = requests.get(baseUrl + cht_sht)

    # store the content for scraping
    soup = BeautifulSoup(req.content)

    if position == "QB":
        qb_data = soup.find_all("div", {"class":"three columns position-QB"})               # grabs the whole ranking list for that position
    elif position == "RB":
        qb_data = soup.find_all("div", {"class":"three columns position-RB"})               # grabs the whole ranking list for that position
    elif position == "WR":
        qb_data = soup.find_all("div", {"class":"three columns position-WR"})               # grabs the whole ranking list for that position
    elif position == "TE":
        qb_data = soup.find_all("div", {"class":"three columns position-TE"})               # grabs the whole ranking list for that position
    else:
        return


    

    # struct used to store this info temorarily
    # TODO save in a Player app / model
    PlayerStruct = namedtuple("PlayerStruct", "Name Link")

    # empty player list that will be returned
    playerList = []
   
    '''
    These scrape fantasy pros for the data of the player in a certain column of the cheat sheet.
    We scrape the name and team code of the player and then the link to the player profile
    
    '''
    qb_data = soup.find_all("div", {"class":"three columns position-QB"})               # grabs the whole ranking list for that position
    qb_name = qb_data[0].contents[3].find_all("a")                                      # grabs the name
    qb_team = qb_data[0].contents[3].find_all("small", {"class":"grey"})                # grabs the team code i.e. "SF"
    qb_link = qb_data[0].contents[3].find_all("a")                                      # grabs all the link to player profiles

    # tracks the actual player links
    # each player has two <a> tags but one is empty
    totalValidLinks = 0

    # for loop fills our player struct with the required info
    # loops through the length of the players scraped
    for i in range(len(qb_name)):
        # holds the href link for the player to fantasypros site
        link = qb_link[i].get('href')

        # if this is one of the valid links
        if link != "#":
            # save the text of our player
            name = qb_name[i].text + ", " + qb_team[totalValidLinks].text

            # increase the valid links found
            totalValidLinks += 1

            # store the iinformation gathered in our player structs
            player = PlayerStruct(name, baseUrl + link)

            # add to our list of players
            playerList.append(player)

    # for link in qb_link:
    #     lnk = link.get('href')
    #     if lnk != "#":
    #         player = PlayerStruct(link.text, baseUrl + link.get('href'))
    #         playerList.append(player)
    
    # return our list of players
    return playerList