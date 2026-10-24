import requests

url='https://openlibrary.org/search.json?q=the+lord+of+the+rings'

params={
    "param1":"value1",
    "pram2":"value2"
}

response=requests.get(url,params=params)

if response.status_code==200:
    data=response.json()
    print(data)
else:
    print(f"Failed get data {response.status_code}")