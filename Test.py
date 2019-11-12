from github import Github

ACCESS_TOKEN = '7d1c0857203613ccc1256c6efeea47bd8b7d809f'
g = Github(ACCESS_TOKEN)

rate_limit = g.get_rate_limit()
rate = rate_limit.search
if rate.remaining == 0:
    print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
else:
    print(f'You have {rate.remaining}/{rate.limit} API calls remaining')

keywords = 'tetris'
query = keywords + '+language:assembly'
result = g.search_repositories(query,'stars', 'desc')
#result = g.search_repositories(query='language:python')

print(f'Found {result.totalCount} repo(s)')
 
for repo in result:
    print(f'login: {repo.owner.login}')
    print(f'repo name: {repo.name}')
    print(f'last update: {repo.updated_at}')