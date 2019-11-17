from github import Github
from datetime import datetime
from datetime import time

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
    return result



#initialze github access
#c_id = '2b9f6e2c97d4a2dc6c67'
#c_secret = '2b9f6e2c97d4a2dc6c67'
access_token = '8e3db69a6c3c3999b38722dfc0419c784adb8f5b'
g = Github(access_token)


api_wait_search(g)
#search microsoft employees
keyword = 'microsoft'
result = company_query(g, keyword)
print(f'Found {result.totalCount} {keyword} employees')
api_wait_search(g)


#print info
for user in result:
    print(f'login: {user.login}')
    print(f'repos_url: {user.repos_url}\n')
