import json, requests 

# function to convert kelvin to celsius
def convertToCelsius(kelvin):
    return round(kelvin - 273.15, 2)

def getWeatherData():
    data = requests.get('http://localhost:5000/get/Weather')
    print(data.text)
    # storeWeatherData((data.text))
    weatherData = json.loads(data.text)
    return {
        'temp': convertToCelsius(weatherData['main']['temp']),
        'feels_like': convertToCelsius(weatherData['main']['feels_like']),
        'humidity': weatherData['main']['humidity'],
        'description': weatherData['weather'][0]['description'],
        'wind_speed': weatherData['wind']['speed']
    }


def storeWeatherData():
    data = getWeatherData()
    weatherData = json.dumps(data)
    file = open('weather.json', 'w')
    file.write(weatherData)

def loadWeatherData():
    file = open('weather.json', 'r')
    weatherData = json.load(file)
    return weatherData
