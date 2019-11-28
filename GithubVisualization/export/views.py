from django.shortcuts import render
from collect.models import *
import json

# Create your views here.
def index(request):
    return render(request, 'export/export.html')

def export1(request):
    microsoft_lang = {}
    google_lang = {}
    microsoft_count = 0
    google_count = 0
    
    a = User.objects.filter(company = 'microsoft')
    for user in a:
        b = Repo.objects.filter(username = user.login)
        for repo in b:
            c = Lang.objects.filter(repo = repo.repo_name)
            print(f'recording repo: {repo.repo_name}')
            for lang in c:
                microsoft_count = microsoft_count + 1
                if (microsoft_lang.__contains__(lang.language) == False):
                    microsoft_lang[lang.language] = 1
                else:
                    microsoft_lang[lang.language] = microsoft_lang[lang.language] + 1
    
    a = User.objects.filter(company = 'google')
    for user in a:
        b = Repo.objects.filter(username = user.login)
        for repo in b:
            c = Lang.objects.filter(repo = repo.repo_name)
            print(f'recording repo: {repo.repo_name}')
            for lang in c:
                google_count = google_count + 1
                if (google_lang.__contains__(lang.language) == False):
                    google_lang[lang.language] = 1
                else:
                    google_lang[lang.language] = google_lang[lang.language] + 1
    
    langs = list(microsoft_lang.keys()) + list(set(google_lang.keys()) - set(microsoft_lang.keys()))
    data = []
    for category in langs:
        print(f'recording category: {category}')
        value = []
        if microsoft_lang.__contains__(category):
            microsoft_value = microsoft_lang[category] / microsoft_count * 100
        else:
            microsoft_value = 0
        if google_lang.__contains__(category):
            google_value = google_lang[category] / google_count * 100
        else:
            google_value = 0
        
        value.append(
            {
                'value' : microsoft_value,
                'company' : 'microsoft'
            }
        )
        value.append(
            {
                'value' : google_value,
                'company' : 'google'
            }
        )
        data.append(
            {
                'categorie' : category,
                'values' : value
            }
        )
    
    with open('data_out.json', 'w') as outfile:
        json.dump(data, outfile)
    

    return render(request, 'export/export.html', {'message': "export 1 done!"})