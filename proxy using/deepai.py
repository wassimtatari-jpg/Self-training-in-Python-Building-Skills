import requests

API_key="You API KEY"

text="Hello i am wassim tatari from morocco tangier"

response=requests.post(
    "https://api.deepai.org/api/summarization",
    data={"text":text},
    headers={"api-key":API_key}
)
data=response.json()

print(data)