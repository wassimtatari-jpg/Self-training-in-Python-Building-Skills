import requests

api_key="Owner key"
city='Tangier'
url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'


response=requests.get(url)
data=response.json()
if response.status_code==200:
    weather=data['weather'][0]["descpription"]
    temp=data['main']['temp']
    print(f"Weather in {city}:{weather}Temprature {temp}")
else:
    print("Error to fetching weather data")

