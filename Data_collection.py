from github import Github

#initialze github access
ACCESS_TOKEN = 'b6ef885e0820f6f9bd58b2a89a163bf3b57877c8'
g = Github(ACCESS_TOKEN)

#search microsoft employees
keyword = 'microsoft'
query = f'"{keyword}" in:org type:user repos:30..50'
result = g.search_users(query)

#restricting number of api calls
max_size = 10
print(f'Found {result.totalCount} user(s)')
if result.totalCount > max_size:
    result = result[:max_size]

#print info
for user in result:
    print(f'login: {user.login}')
    print(f'repos_url: {user.repos_url}\n')