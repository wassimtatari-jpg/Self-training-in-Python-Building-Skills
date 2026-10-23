import requests

response=requests.get('https://openlibrary.org/search/authors.json?q=J.%20R.%20R.%20Tolkien')
print(response.status_code)
print("-"*25)
print(response.json().keys())
print("-"*25)
print(response.json()["docs"][0])
print("-"*25)
print(response.json()["docs"][0]['name'])
print("-"*25)
authors=response.json()["docs"]

for book in authors:
    print(book.get("name"),book.get("work_count","unkown"))
