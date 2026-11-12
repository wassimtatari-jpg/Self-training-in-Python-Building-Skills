import requests

url='http://api.open-notify.org/iss-now.json'

response=requests.get(url)
data=response.json()

if response.status_code==200:
    possition=data['iss_position']
    print(f"The ISS is in coodinates longitude:{possition['longitude']} latitude:{possition['latitude']}")
else:
    print("Error fecting ISS data")


