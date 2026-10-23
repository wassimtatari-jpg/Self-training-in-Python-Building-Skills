import requests


response=requests.get("https://openlibrary.org/search.json?q=The+Hobbit")
print(response.json().keys())
print(response.json()['docs'][0].keys())
print(response.status_code)


books=response.json()['docs'][0:5]

for book in books:
    print(book['title'],book['first_publish_year'])

books=response.json()['docs'][0]

for key,value in books.items():
    print(key,type(value))

print("-"*35)
books=response.json()['docs'][0]
for key,value in books.items():
    if isinstance(value,list):
       print(key,(value))
print("-"*25)
books=response.json()['docs'][0]
for key,value in books.items():
    if isinstance(value,str):
        print(key,value)
print("-"*25)
books=response.json()['docs'][0]
for key,value in books.items():
    if isinstance(value,int):
        print(key,value)
print("-"*25)
books=response.json()['docs'][0]
for key,value in books.items():
    if isinstance(value,dict):
        print(key,value)
print("-"*25)
books=response.json()['docs'][0]
for key,value in books.items():
    if isinstance(value,float):
        print(key,value)