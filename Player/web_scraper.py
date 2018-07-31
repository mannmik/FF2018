import json
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from collections import namedtuple

def cheat_sheet_scraper(position):

     # the base url info we are using to scrape the cheatsheet
    baseUrl = "https://www.fantasypros.com"
    cht_sht = "/nfl/cheatsheets/"

    # we make a get request to fantasy webpage and store the content
    req = requests.get(baseUrl + cht_sht)

    # store the content for scraping
    soup = BeautifulSoup(req.content, "html.parser")

    if position == "QB":
        player_data = soup.find_all("div", {"class":"three columns position-QB"})               # grabs the whole ranking list for that position
    elif position == "RB":
        player_data = soup.find_all("div", {"class":"three columns position-RB"})               # grabs the whole ranking list for that position
    elif position == "WR":
        player_data = soup.find_all("div", {"class":"three columns position-WR"})               # grabs the whole ranking list for that position
    elif position == "TE":
        player_data = soup.find_all("div", {"class":"three columns position-TE"})               # grabs the whole ranking list for that position
    else:
        return


    

    # struct used to store this info temorarily
    # TODO save in a Player app / model
    PlayerStruct = namedtuple("PlayerStruct", "Rank Name Link")

    # empty player list that will be returned
    playerList = []
   
    '''
    These scrape fantasy pros for the data of the player in a certain column of the cheat sheet.
    We scrape the name and team code of the player and then the link to the player profile
    
    '''
    # player_data = soup.find_all("div", {"class":"three columns position-QB"})               # grabs the whole ranking list for that position
    player_name = player_data[0].contents[3].find_all("a")                                      # grabs the name
    player_team = player_data[0].contents[3].find_all("small", {"class":"grey"})                # grabs the team code i.e. "SF"
    player_link = player_data[0].contents[3].find_all("a")                                      # grabs all the link to player profiles
   
    # tracks the actual player links
    # each player has two <a> tags but one is empty
    totalValidLinks = 0

    rnk = 0
    # for loop fills our player struct with the required info
    # loops through the length of the players scraped
    for i in range(len(player_name)):
        # holds the href link for the player to fantasypros site
        link = player_link[i].get('href')

        # if this is one of the valid links
        if link != "#":
           
            rnk = totalValidLinks + 1

            # save the text of our player
            name =  player_name[i].text + ", " + player_team[totalValidLinks].text
            
            # increase the valid links found
            totalValidLinks += 1

            # store the iinformation gathered in our player structs
            player = PlayerStruct(rnk, name, baseUrl + link)

            # add to our list of players
            playerList.append(player)

    # return our list of players
    return playerList


def fantasy_news_scraper():
     # the base url info we are using to scrape the player fantasy news
    baseUrl = "https://www.fantasypros.com"

    # we want fantasy football news
    league = "/nfl/"

    # struct used to store this info temorarily
    # TODO save in a Player app / model
    PlayerNews = namedtuple("PlayerNews", "Text Link")
     # we make a get request to fantasy webpage and store the content
    req = requests.get(baseUrl + league)

    # store the content for scraping
    soup = BeautifulSoup(req.content, "html.parser")

    player_news = []

    fantasy_news = soup.find_all("div", {"id":"player-news-nfl"})
    nfl_players = fantasy_news[0].find_all("div", {"class":"extra"})

    for i in nfl_players:

        player_link = baseUrl + i.find('a')['href']
        player_text = i.find('a').text
        #test_player = fantasy_news.
        player_news.append(PlayerNews(player_text, player_link))

   
    return player_news      
