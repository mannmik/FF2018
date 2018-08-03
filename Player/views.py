from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from FF2018 import api_services
from bs4 import BeautifulSoup
from collections import namedtuple
from . import web_scraper
from NFLteams.models import NFL_Team
from . models import Player
import requests
import json
import pandas as panda 
import numpy as np 


def CheatSheet(request):
   
    qb_list = web_scraper.cheat_sheet_scraper("QB")
    rb_list = web_scraper.cheat_sheet_scraper("RB")
    wr_list = web_scraper.cheat_sheet_scraper("WR")
    te_list = web_scraper.cheat_sheet_scraper("TE")
    
    qbs = []

    PlayerTable = namedtuple("PlayerTable", "qb_name qb_link rb_name rb_link wr_name wr_link te_name te_link")

    for i in range(len(rb_list)):
        if i <= 36:
            qbs.append(PlayerTable(str(qb_list[i][0]) +". " + qb_list[i][1], qb_list[i][2], str(rb_list[i][0]) + ". " + rb_list[i][1], rb_list[i][2], 
            str(wr_list[i][0]) + ". " + wr_list[i][1], wr_list[i][2], str(te_list[i][0])  + ". " + te_list[i][1], te_list[i][2] ))
        else:
            qbs.append(PlayerTable("", "", str(rb_list[i][0]) + ". " + rb_list[i][1], rb_list[i][2], 
            str(wr_list[i][0]) + ". " + wr_list[i][1], wr_list[i][2], "", "" ))

    #link = api_services.cheat_sheet_scraper()
    return render(request, 'cheatsheet.html', {'qbs':qbs})


def PlayerNews(request):
    news = web_scraper.fantasy_news_scraper()

    return render(request, "success.html", {"news":news})  


def Player_Init(request):
    if request.user.is_staff:

        qbs = panda.read_excel('QB.xlsx')
        rbs = panda.read_excel('RB.xlsx')
        wrs = panda.read_excel('WR.xlsx')
        te = panda.read_excel('TE.xlsx')
        #dst = panda.read_excel('DST.xlsx')
        kickers = panda.read_excel('K.xlsx')

        # loop through our qbs and save them in Player models
        for i in range(len(qbs['Rank'])):
            new_player = Player()

            new_player.fullName = qbs.loc[i, 'Name']
            new_player.position = 'QB'
            new_player.positionRank = qbs.loc[i, 'Rank']
            team = NFL_Team.objects.get(code=qbs.loc[i, 'Team'])
            new_player.team = team

            new_player.save()

        # add all players for each position
        add_player_list('RB', rbs)
        add_player_list('WR', wrs)
        add_player_list('DST', dst)
        add_player_list('TE', te)
        add_player_list('K', kickers)
        

        qb_list = Player.objects.filter(position='QB')
        rb_list = Player.objects.filter(position='RB')
        wr_list = Player.objects.filter(position='WR')
        te_list = Player.objects.filter(position='TE')
        dst_list = Player.objects.filter(position='DST')
        k_list = Player.objects.filter(position='K')
        return render(request, "success.html", {"news":k_list})
    else:
        return render(request, 'login.html' , {"error": "You must be logged in to complete this action."})

def add_player_list(position, list):
     for i in range(len(list['Name'])):
            new_player = Player()

            player_str = list.loc[i, 'Name']
            info = player_str.split(" - ")

            new_player.fullName = info[0]
            new_player.position = position
            new_player.positionRank = i + 1
            if info[1] > "":
                team = NFL_Team.objects.get(code=info[1])
                new_player.team = team

                new_player.save()

def del_player_by_pos(pos):
    Player.objects.filter(position=pos).delete()