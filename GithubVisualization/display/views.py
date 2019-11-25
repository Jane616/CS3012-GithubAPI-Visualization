from django.shortcuts import render
import os
from GithubVisualization import settings
import json
from django.http.response import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'display/display.html')

def return_json(request):
    file = open(os.path.join(settings.BASE_DIR, 'export/data.json'))
    j = json.load(file)
    return JsonResponse(list(j), safe=False)