import requests

with open("example.txt",'rb') as f:
    file={"file":f}
    response=requests.post('https://httpbin.org/post',files=file)
print(response.json())