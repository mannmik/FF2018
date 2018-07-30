from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from FF2018 import api_services
from bs4 import BeautifulSoup
from collections import namedtuple
from . import web_scraper
import requests
import json

def CheatSheet(request):
   
    qb_list = web_scraper.cheat_sheet_scraper("QB")
    rb_list = web_scraper.cheat_sheet_scraper("RB")
    wr_list = web_scraper.cheat_sheet_scraper("WR")
    te_list = web_scraper.cheat_sheet_scraper("TE")
    
    players = []

    PlayerTable = namedtuple("PlayerTable", "qb_name qb_link rb_name rb_link wr_name wr_link te_name te_link")

    for i in range(len(rb_list)):
        if i <= 36:
            players.append(PlayerTable(qb_list[i][0], qb_list[i][1], rb_list[i][0], rb_list[i][1], wr_list[i][0], wr_list[i][1], te_list[i][0], te_list[i][1] ))
        else:
            players.append(PlayerTable("", "", rb_list[i][0], rb_list[i][1], wr_list[i][0], wr_list[i][0], "", "" ))

    #link = api_services.cheat_sheet_scraper()
    return render(request, 'cheatsheet.html', {'players':players})
