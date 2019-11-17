from github import Github

#initialze github access
print('please input your username: ')
user_name = input()
print('please input your password: ')
password = input()
g = Github(user_name, password)

#get remaining rate limit
rate_limit = g.get_rate_limit()
rate = rate_limit.search
if rate.remaining == 0:
    print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
else:
    print(f'You have {rate.remaining}/{rate.limit} API calls remaining')

#construct and perform a query
keywords = 'tetris'
query = keywords + '+language:assembly'
result = g.search_repositories(query,'stars', 'desc')

#access information returned by query
print(f'Found {result.totalCount} repo(s)')
for repo in result:
    print(f'login: {repo.owner.login}')
    print(f'repo name: {repo.name}')
    print(f'last update: {repo.updated_at}')
