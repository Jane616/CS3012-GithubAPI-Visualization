from github import Github
from datetime import datetime
from datetime import time

#class for storing language information
class Lang:
  def __init__(self, name, count):
    self.name = name
    self.count = count

#class for storing github account information
class Account:
  def __init__(self, login, repos):
    self.login = login
    self.repos = repos
    self.languages = [] #a list of languages calculated from account's repos

#pause program if about to exceed rate limit
def api_wait_search(git):
  limits = git.get_rate_limit()
  print(f'remaining limit: {limits.search.remaining}')
  if limits.search.remaining <= 2:
    seconds = (limits.search.reset - datetime.now()).total_seconds()
    print ("Waiting for %d seconds ..." % (seconds))
    time.sleep(seconds)
    print ("Done waiting - resume!")


#get list of company employees
def company_query(g, keyword):
    query = f'"{keyword}" in:org type:user repos:30..50'
    result = g.search_users(query)
    accounts = []
    for user in result:
      accounts.append(Account(user.login, user.repos_url))
    return accounts



#initialze github access
print('please input your username: ')
user_name = input()
print('please input your password: ')
password = input()
g = Github(user_name, password)


api_wait_search(g)
#search microsoft employees
keyword = 'microsoft'
result = company_query(g, keyword)
print(f'Found {len(result)} {keyword} employees')
api_wait_search(g)

for user in result[:2]:
  print(f'login: {user.login}')
  print(f'repos: {user.repos}')
