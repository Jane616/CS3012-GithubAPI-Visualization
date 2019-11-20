from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from subprocess import run, PIPE
import sys
import os
import logging

# Create your views here.

def index(request):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    FILE_DIR = os.path.join(BASE_DIR, 'collect/test.py')
    out = run([sys.executable, FILE_DIR], shell= False, stdout=PIPE)
    print(f'\n{out.stdout}\n')
    context = {
        'message': out.stdout.decode('utf-8'),
    }
    return render(request, 'collect/collect.html', context)