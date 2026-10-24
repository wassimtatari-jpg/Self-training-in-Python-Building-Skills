import requests

file={"file":open("example.txt","rb")}

response=requests.post('https://httpbin.org/post',files=file)

file["file"].close()
print(response.json())