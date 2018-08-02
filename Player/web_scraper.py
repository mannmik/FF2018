import json
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from collections import namedtuple

def cheat_sheet_scraper(position):

     # the base url info we are using to scrape the cheatsheet
    ff_Pro_baseUrl = "https://www.fantasypros.com"
    cht_sht = "/nfl/cheatsheets/"

    # we make a get request to fantasy webpage and store the content
    req = requests.get(ff_Pro_baseUrl + cht_sht)

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
   
    """
    These scrape fantasy pros for the data of the player in a certain column of the cheat sheet.
    We scrape the name and team code of the player and then the link to the player profile
    
    """
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
        link = player_link[i].get("href")

        # if this is one of the valid links
        if link != "#":
           
            rnk = totalValidLinks + 1

            # save the text of our player
            name =  player_name[i].text + ", " + player_team[totalValidLinks].text
            
            # increase the valid links found
            totalValidLinks += 1

            # store the iinformation gathered in our player structs
            player = PlayerStruct(rnk, name, ff_Pro_baseUrl + link)

            # add to our list of players
            playerList.append(player)

    # return our list of players
    return playerList


def fantasy_news_scraper():
     # the base url info we are using to scrape the player fantasy news from ff pros
    ff_Pro_baseUrl = "https://www.fantasypros.com"

    yahoo_ff_baseUrl = "https://football.fantasysports.yahoo.com/"

    # we want fantasy football news
    # league = "/nfl/"

    urls = [ff_Pro_baseUrl, yahoo_ff_baseUrl]

    # struct used to store this info temorarily
    # TODO save in a Player app / model
    PlayerNews = namedtuple("PlayerNews", "Text Link")

    player_news = []

    ff_pros_news = []
    rotoworld_news = []
    nfl_com_news = []

    for url in urls:

        # we make a get request to fantasy webpage and store the content
        req = requests.get(url)

        # store the content for scraping
        soup = BeautifulSoup(req.content, "html.parser")

        if url == ff_Pro_baseUrl:

            fantasy_news = soup.find_all("div", {"id":"player-news-nfl"})
            nfl_players = fantasy_news[0].find_all("div", {"class":"extra"})

            for i in nfl_players:

                player_link = ff_Pro_baseUrl + i.find("a")["href"]
                player_text = i.find("a").text
               
                ff_pros_news.append(PlayerNews(player_text, player_link))

        elif url == yahoo_ff_baseUrl:
            # we make a get request to fantasy webpage and store the content
            req = requests.get(url)

            # store the content for scraping
            soup = BeautifulSoup(req.content, "html.parser")

            fantasy_news = soup.find_all("section", {"id":"playernotes"})
            nfl_players_news = fantasy_news[0].contents[3].find_all('li')

            for i in nfl_players_news:
                player_link = i.find("a")["href"]
                player_text= i.find("a").text

                rotoworld_news.append(PlayerNews(player_text, player_link))
     
    player_news.append(ff_pros_news)
    player_news.append(rotoworld_news)
   


    return player_news      


def strength_of_schedule_scraper():
    
    # baseUrl = "https://fftoolbox.scoutfantasysports.com"
    # params = "?type=d"
    # url = baseUrl

    # # we make a get request to fantasy webpage and store the content
    # req = requests.get(url)

    # # store the content for scraping
    # soup = BeautifulSoup(req.content, "html.parser")

    # sos_table = soup.find_all("tr", {"class":"c"})
    # sos_info = sos_table.find_all("a")

    # baseUrl = "https://www.fantasypros.com/nfl"
    # params = "/strength-of-schedule.php?position=QB"
    # url = baseUrl + params

    # # we make a get request to fantasy webpage and store the content
    # req = requests.get(url)

    # # store the content for scraping
    # soup = BeautifulSoup(req.content, "html.parser")

    # rankings = soup.find("div", {"class":"mobile-table"})

    teams = []
    teams.append({"Team":"BUF", "QB":1, "RB":10, "WR":17})
    teams.append({"Team":"ARI", "QB":2, "RB":6, "WR":20})
    teams.append({"Team":"JAC", "QB":3, "RB":27, "WR":4})
    teams.append({"Team":"PHI", "QB":4, "RB":12, "WR":19})
    teams.append({"Team":"NO", "QB":5, "RB":19, "WR":16})
    teams.append({"Team":"LAC", "QB":6, "RB":14, "WR":14})
    teams.append({"Team":"DEN", "QB":7, "RB":5, "WR":23})
    teams.append({"Team":"DAL", "QB":8, "RB":23, "WR":12})
    teams.append({"Team":"PIT", "QB":9, "RB":21, "WR":11})
    teams.append({"Team":"MIN", "QB":10, "RB":13, "WR":7})
    teams.append({"Team":"BAL", "QB":11, "RB":11, "WR":26})
    teams.append({"Team":"CHI", "QB":12, "RB":3, "WR":25})
    teams.append({"Team":"NYG", "QB":13, "RB":31, "WR":9})
    teams.append({"Team":"OAK", "QB":14, "RB":29, "WR":2})
    teams.append({"Team":"ATL", "QB":15, "RB":16, "WR":3})
    teams.append({"Team":"TEN", "QB":16, "RB":17, "WR":15})
    teams.append({"Team":"SF", "QB":17, "RB":24, "WR":18})
    teams.append({"Team":"TB", "QB":18, "RB":20, "WR":8})
    teams.append({"Team":"KC", "QB":19, "RB":15, "WR":30})
    teams.append({"Team":"CAR", "QB":20, "RB":22, "WR":1})
    teams.append({"Team":"MIA", "QB":21, "RB":8, "WR":5})
    teams.append({"Team":"LAR", "QB":22, "RB":30, "WR":6})
    teams.append({"Team":"GB", "QB":23, "RB":32, "WR":10})
    teams.append({"Team":"WAS", "QB":24, "RB":28, "WR":29})
    teams.append({"Team":"NYJ", "QB":25, "RB":26, "WR":27})
    teams.append({"Team":"HOU", "QB":26, "RB":4, "WR":28})
    teams.append({"Team":"DET", "QB":27, "RB":2, "WR":13})
    teams.append({"Team":"NE", "QB":28, "RB":1, "WR":32})
    teams.append({"Team":"SEA", "QB":29, "RB":18, "WR":24})
    teams.append({"Team":"CLE", "QB":30, "RB":9, "WR":22})
    teams.append({"Team":"CIN", "QB":31, "RB":25, "WR":21})
    teams.append({"Team":"IND", "QB":32, "RB":7, "WR":31})

    sos_info = teams

  

    return sos_info
