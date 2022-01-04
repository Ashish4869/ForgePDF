import json, requests

# function to convert kelvin to celsius
def convertToCelsius(kelvin):
    return round(kelvin - 273.15, 2)

def getWeatherData():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=mangalore&appid=f5990901916de44b03db0a2d1c42140d'
    response = requests.get(url)
    response.raise_for_status()
    weatherData = json.loads(response.text)
    return {
        'temp': convertToCelsius(weatherData['main']['temp']),
        'feels_like': convertToCelsius(weatherData['main']['feels_like']),
        'humidity': weatherData['main']['humidity'],
        'description': weatherData['weather'][0]['description'],
        'wind_speed': weatherData['wind']['speed']
    }

def storeWeatherData():
    weatherData = getWeatherData()
    file = open('weather.json', 'w')
    file.write(json.dumps(weatherData))

def loadWeatherData():
    file = open('weather.json', 'r')
    weatherData = json.load(file)
    return weatherData
