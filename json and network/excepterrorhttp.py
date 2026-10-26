import http.client
try:
    conn=http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    conn.request("GET","post/1")
    response=conn.getresponse()
    print(response.status,response.reason)
    data=response.read().decode('utf-8')
    print(data)
except http.client.HTTPException as er:
    print(er)
except Exception as er:
    print(er)
finally:
    conn.close()