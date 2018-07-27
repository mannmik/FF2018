from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from FF2018 import api_services
import json

def Update(request):
    if request.user.is_staff:
        teams = api_services.get_nfl_teams()
        #return HttpResponse(teams['NFLTeams'])
        teamList = []
        for i in teams["NFLTeams"]:
            teamList.append(i['code'])

        return render(request, 'success.html', {"teamList":teamList} )
    else:
        return redirect('home')
