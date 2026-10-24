import requests

response=requests.get('https://openlibrary.org/search.json?q=titanic')

print(response.status_code)
print(response.reason)
print(response.ok)
print(response.headers)
print(response.headers['Connection'])


