from github import Github
from datetime import datetime
import time
from github.GithubException import BadCredentialsException

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

#pause program if rate limit is not full
def api_wait_search(git):
  limits = git.get_rate_limit()
  print(f'remaining limit: {limits.search.remaining}')
  if limits.search.remaining < 30:
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
api_wait_search(g)
keyword = 'google'
google_users = company_query(g, keyword)
print(f'Found {len(google_users)} {keyword} employees')

for user in google_users[:2]:
  print(f'login: {user.login}')
  print(f'repos: {user.repos}')
