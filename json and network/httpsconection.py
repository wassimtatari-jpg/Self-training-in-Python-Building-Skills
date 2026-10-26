import http.client

conn=http.client.HTTPSConnection("jsonplaceholder.typicode.com")

conn.request("GET","/posts/1")

response=conn.getresponse()

print(response.status,response.reason)

data=response.read().decode("utf-8")

print(data)


headres=response.getheaders()

for header in headres:
    print(f'{header[0]}:{header[1]}')
conn.close()