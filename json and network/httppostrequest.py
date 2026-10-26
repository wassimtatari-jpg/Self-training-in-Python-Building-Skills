import http.client
import json

paydata=json.dumps({
    "name":"wassim",
    "age":39,
    "user":19
})
header={
    "content":"application/json"
}

conn=http.client.HTTPSConnection("jsonplaceholder.typicode.com")

conn.request("POST","post1/",body=paydata,headers=header)

response=conn.getresponse()

print(response.status,response.reason)

data=response.read().decode("utf-8")
print(data)

conn.close()