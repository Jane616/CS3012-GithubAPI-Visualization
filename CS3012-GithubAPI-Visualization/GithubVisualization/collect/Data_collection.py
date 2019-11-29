from github import Github
from datetime import datetime
import time
from github.GithubException import BadCredentialsException
import urllib.request, json
from .models import *

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


