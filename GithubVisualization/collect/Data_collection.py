from github import Github
from datetime import datetime
import time
from github.GithubException import BadCredentialsException
import urllib.request, json
from .models import *
#from Database_store import *

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

#class for storing language information
class Lang:
  def __init__(self, name, count):
    self.name = name
    self.count = count

#class for storing repository information
class Repo:
  def __init__(self, name, stargazer):
    self.name = name
    self.stargazer = stargazer
    self.languages = []

#class for storing github account information
class Account:
  def __init__(self, login, repos):
    self.login = login
    self.repos_url = repos
    self.repos = [] #a list of accounts' repos

#pause program if rate limit is not full
def api_wait_search(git):
  limits = git.get_rate_limit()
  print(f'remaining limit: {limits.search.remaining}')
  if limits.search.remaining <= 4:
    seconds = (limits.search.reset - datetime.now()).total_seconds()
    print ("Waiting for %d seconds ..." % (seconds))
    time.sleep(seconds)
    print ("Done waiting - resume!")


#get list of company employees
def company_query(g, keyword):
    query = f'"{keyword}" in:org type:user repos:30..35'
    result = g.search_users(query)
    accounts = []
    for user in result:
      accounts.append(Account(user.login, user.repos_url))
    return accounts

def repo_query(g, user):
    query = f'user:"{user}""'
    result = g.get_user(login = user).get_repos()
    #result = g.search_repositories(query)
    return result
    count = 0
    for repo in result:
      repo_name = repo.name
      stargazer = int(repo.stargazers_count)
      r = Repo(username = user, repo_name = repo_name, stargazer = stargazer)
      r.save()
      #access language information
      with urllib.request.urlopen(repo.languages_url) as url:
        data = json.loads(url.read().decode())
        for i in data.keys():
          if data[i].isdigit():
            c = int(data[i])
            l = Lang(repo = repo.name, language = i, count = c)
            l.save()
      count = count + 1
      if (count > 25):
        api_wait_search(g)
        count = 0
      

    return

#initialze github access
"""
while True:
  print('please input your username: ')
  user_name = input()
  print('please input your password: ')
  password = input()
  try:
    g = Github(user_name, password)
    g.get_rate_limit() #test if it raise BadCredentialsException
  except BadCredentialsException:
      print('login information not valid!')
      continue
  else:
      print('login success')
      break

#search microsoft employees
api_wait_search(g)
keyword = 'microsoft'
microsoft_users = company_query(g, keyword)
print(f'Found {len(microsoft_users)} {keyword} employees')

#search google employees
limits = g.get_rate_limit()
print(f'remaining limit: {limits.search.remaining}')
keyword = 'google'
google_users = company_query(g, keyword)
print(f'Found {len(google_users)} {keyword} employees')

limits = g.get_rate_limit()
print(f'remaining limit: {limits.search.remaining}')

for user in google_users[:2]:
  print(f'login: {user.login}')
  print(f'repos: {user.repos_url}')
  repo_query(g, user.login)

"""
