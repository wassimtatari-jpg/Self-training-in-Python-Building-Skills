import requests

google_api='#########################'
address="Tangier,Morocco"
url=f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_api}'

response=requests.get(url)
data=response.json()
print(data)
if data["status"]=="OK":
    location=data['results'][0]['geometry']['location']
    lat=location['lat']
    lng=location['lng']
    print(f"{lat},{lng}")
else:
    print("erorr")