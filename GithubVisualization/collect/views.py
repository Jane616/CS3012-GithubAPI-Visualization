from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from subprocess import run, PIPE
import sys
import os
import logging
from .Data_collection import *
from .models import *
import time
import urllib.request, json
from urllib.request import Request
import requests

# Create your views here.

def index(request):
    return render(request, 'collect/collect.html')

def getdata(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        g = Github(username, password)
        g.get_rate_limit() #test if it raise BadCredentialsException
    except BadCredentialsException:
        print('login information not valid!')
        return render(request, 'collect/collect.html', {'message': "login information not valid!"})


    user_name = 'Jane616'
    password = 'Jane@990616'
    g = Github(user_name, password)

    
    api_wait_search(g)
    keyword = 'microsoft'
    microsoft_users = company_query(g, keyword)
    print(f'Found {len(microsoft_users)} {keyword} employees')
    
    keyword = 'google'
    google_users = company_query(g, keyword)
    print(f'Found {len(google_users)} {keyword} employees')

    print('new sleeping for 50 seconds to reset search limit')
    time.sleep(50)

    print(microsoft_users[len(microsoft_users) - 1].login)

    
    for user in microsoft_users:
        u = User(company = "microsoft", login = user.login)
        u.save()

    for user in google_users:
        u = User(company = "google", login = user.login)
        u.save()    
    
    count = 0
    users = google_users + microsoft_users
    for user in users:
        result = repo_query(g, user.login)
        print(f'recording user: {user.login}')
        print(f'repo count: {result.totalCount}')

        for repo in result:
            repo_name = repo.name
            print(f'recording repo: {repo_name}')
            stargazer = int(repo.stargazers_count)
            r = Repo(username = user.login, repo_name = repo_name, stargazer = stargazer)
            r.save()

            #access language information
            response = requests.get(repo.languages_url,
                            auth=requests.auth.HTTPBasicAuth(user_name, password))
            data = response.json()
            for i in data.keys():
                if str(data[i]).isdigit():
                    c = int(data[i])
                    l = Lang(repo = repo.name, language = i, count = c)
                    l.save()
                
            count = count + 1

            if (count > 25):
                api_wait_search(g)
                count = 0
    
    return render(request, 'collect/collect.html', {'message': "done!"})
