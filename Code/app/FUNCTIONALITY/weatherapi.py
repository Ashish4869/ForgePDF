import json, requests

# function to convert kelvin to celsius
def convertToCelsius(kelvin):
    return round(kelvin - 273.15, 2)

url = 'https://api.openweathermap.org/data/2.5/weather?q=mangalore&appid=f5990901916de44b03db0a2d1c42140d'
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)

print('temp', convertToCelsius(weatherData['main']['temp']))
print('feels_like', convertToCelsius(weatherData['main']['feels_like']))
print('humidity', weatherData['main']['humidity'], '%')
print('description', weatherData['weather'][0]['description'])
print('wind_speed', weatherData['wind']['speed'])

