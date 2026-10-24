import requests

url="https://api.example.com/data"

data={
    "name":"wassim tatari",
    "nationalety":"syrian",
    "age":39
}


response=requests.post(url,json=data)


if response.status_code==200:
    print(response.json())

else:
    print(f"Failed {response.status_code}")