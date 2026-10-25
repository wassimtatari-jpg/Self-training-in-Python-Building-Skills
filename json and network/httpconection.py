import http.client

conn=http.client.HTTPConnection("example.com")

conn.request("GET","/")

response=conn.getresponse()

print(response.status,response.reason)

conn.close()