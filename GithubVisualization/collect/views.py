from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from subprocess import run, PIPE
import sys
import os
import logging
from .Data_collection import *
from .models import *

# Create your views here.

def index(request):
    #BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    #FILE_DIR = os.path.join(BASE_DIR, 'collect/test.py')
    #out = run([sys.executable, FILE_DIR], shell= False, stdout=PIPE)
    #print(f'\n{out.stdout}\n')
    user_name = 'Jane616'
    password = 'Jane@990616'
    g = Github(user_name, password)

    api_wait_search(g)
    keyword = 'microsoft'
    microsoft_users = company_query(g, keyword)
    print(f'Found {len(microsoft_users)} {keyword} employees')

    api_wait_search(g)
    keyword = 'google'
    google_users = company_query(g, keyword)
    print(f'Found {len(google_users)} {keyword} employees')

    for user in microsoft_users:
        u = User(company = "microsoft", login = user.login)
        u.save()

    for user in google_users:
        u = User(company = "google", login = user.login)
        u.save()
    #print(User.objects.all())
    
    return render(request, 'collect/collect.html', {'message': "done!"})