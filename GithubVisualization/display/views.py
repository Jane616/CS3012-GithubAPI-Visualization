from django.shortcuts import render
import os
from GithubVisualization import settings
import json
from django.http.response import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'display/display.html')

def display1(request):
    return render(request, 'display/display1.html')

def display2(request):
    return render(request, 'display/display2.html')

def display3(request):
    return render(request, 'display/display3.html')

def return_json_1(request):
    file = open(os.path.join(settings.BASE_DIR, 'data_out.json'))
    j = json.load(file)
    return JsonResponse(list(j), safe=False)

def return_json_2(request):
    file = open(os.path.join(settings.BASE_DIR, 'data_out_2.json'))
    j = json.load(file)
    return JsonResponse(list(j), safe=False)

def return_json_3(request):
    file = open(os.path.join(settings.BASE_DIR, 'data_out_3.json'))
    j = json.load(file)
    return JsonResponse(list(j), safe=False)