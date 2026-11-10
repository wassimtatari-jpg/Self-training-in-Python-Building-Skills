import requests

owner_repo="wassimtatari-jpg"

repo_name="Shapes-Application"


url=f'https://api.github.com/repos/{owner_repo}/{repo_name}'

response=requests.get(url)
data=response.json()

if response.status_code==200:
    print(f"Repository:{data['name']}")
    print(f"Description:{data['description']}")
    print(f"Stars:{data['stargazers_count']}")
else:
    print('Error Fetching Repository information')

