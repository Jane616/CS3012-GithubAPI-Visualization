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
    

    return render(request, 'export/export.html', {'message1': "export 1 done!"})

def export23(request):
    lang_count_ms = {}
    lang_count_gg = {}
    good_at_ms = {}
    good_at_gg = {}

    #extract info on microsoft employees
    a = User.objects.filter(company = 'microsoft')
    for auser in a:
        user = []
        langcount = 0
        b = Repo.objects.filter(username = auser.login)
        print(f'recording user: {auser.login}')
        for repo in b:
            c = Lang.objects.filter(repo = repo.repo_name)
            print(f'recording repo: {repo.repo_name}')
            for lang in c:
                isfound = 0
                for item in user:
                    if item['lang'] == lang.language:
                        isfound = 1
                        item['count'] = item['count'] + lang.count
                        break
                    
                if isfound == 0:
                    #if this language's info is not yet recorded
                    langcount = langcount + 1
                    user.append(
                        {
                            'lang' : lang.language,
                            'count' : lang.count
                        }
                    )
        print(user)
        if langcount == 0:
            continue
        #record the number of languages a user is familliar with
        if lang_count_ms.__contains__(langcount):
            lang_count_ms[langcount] = lang_count_ms[langcount] + 1
        else:
            lang_count_ms[langcount] = 1
        
        #record the language with the largest number of files 
        #as the language that this user is good at
        good_at = user[0]['lang']
        highest_count = user[0]['count']
        for info in user:
            if info['count'] >  highest_count:
                good_at = info['lang']
                highest_count = info['count']
            
        if good_at_ms.__contains__(good_at):
            good_at_ms[good_at] = good_at_ms[good_at] + 1
        else:
            good_at_ms[good_at] = 1
        


    #extract info on google employees
    a = User.objects.filter(company = 'google')
    for auser in a:
        user = []
        langcount = 0
        b = Repo.objects.filter(username = auser.login)
        for repo in b:
            c = Lang.objects.filter(repo = repo.repo_name)
            print(f'recording repo: {repo.repo_name}')
            for lang in c:
                isfound = 0
                for item in user:
                    if item['lang'] == lang.language:
                        isfound = 1
                        item['count'] = item['count'] + lang.count
                        break
                    
                if isfound == 0:
                    #if this language's info is not yet recorded
                    langcount = langcount + 1
                    user.append(
                        {
                            'lang' : lang.language,
                            'count' : lang.count
                        }
                    )

        #record the number of languages a user is familliar with
        if lang_count_gg.__contains__(langcount):
            lang_count_gg[langcount] = lang_count_gg[langcount] + 1
        else:
            lang_count_gg[langcount] = 1
        
        #record the language with the largest number of files 
        #as the language that this user is good at
        good_at = user[0]['lang']
        highest_count = user[0]['count']
        for info in user:
            if info['count'] >  highest_count:
                good_at = info['lang']
                highest_count = info['count']
            
        if good_at_gg.__contains__(good_at):
            good_at_gg[good_at] = good_at_gg[good_at] + 1
        else:
            good_at_gg[good_at] = 1

    #export json on how many languages a employee is familliar with
    counts = list(lang_count_ms.keys()) + list(set(lang_count_gg.keys()) - set(lang_count_ms.keys()))
    data = []

    for count in counts:
        print(f'recording count: {count}')
        value = []
        if lang_count_ms.__contains__(count):
            ms_value = lang_count_ms[count]
        else:
            ms_value = 0
        if lang_count_gg.__contains__(count):
            gg_value = lang_count_gg[count]
        else:
            gg_value = 0

        value.append(
            {
                'value' : ms_value,
                'company' : 'microsoft'
            }
        )
        value.append(
            {
                'value' : gg_value,
                'company' : 'google'
            }
        )
        data.append(
            {
                'categorie' : count,
                'values' : value
            }
        )
    
    with open('data_out_2.json', 'w') as outfile:
        json.dump(data, outfile)

    #export json on the language the user is good at
    langs = list(good_at_ms.keys()) + list(set(good_at_gg.keys()) - set(good_at_ms.keys()))
    data = []

    for lang in langs:
        print(f'recording lang: {lang}')
        value = []
        if good_at_ms.__contains__(lang):
            ms_value = good_at_ms[lang]
        else:
            ms_value = 0
        if good_at_gg.__contains__(lang):
            gg_value = good_at_gg[lang]
        else:
            gg_value = 0

        value.append(
            {
                'value' : ms_value,
                'company' : 'microsoft'
            }
        )
        value.append(
            {
                'value' : gg_value,
                'company' : 'google'
            }
        )
        data.append(
            {
                'categorie' : lang,
                'values' : value
            }
        )
    
    with open('data_out_3.json', 'w') as outfile:
        json.dump(data, outfile)


    return render (request, 'export/export.html', {'message2': "export 2 3 done!"})