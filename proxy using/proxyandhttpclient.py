import http.client

host='10.10.1.10'


port=3128


url='httpbin.org'

path='/ip'

conn=http.client.HTTPSConnection(host,port)

conn.set_tunnel(url)

conn.request("GET",path)

response=conn.getresponse()

print(response.status,response.reason)

print(response.read().decode('utf-8'))

conn.close()