import json, requests 


def getWeatherData():
    try:
        data = requests.get('http://localhost:5000/weather')
        weatherData = json.loads(data.text)
    except:
        data = json.dumps({"error": "Could not connect to the server, please run the server first"})
        weatherData = json.loads(data)
    json.dump(weatherData, open('weather.json', 'w'))

def loadWeatherData():
    file = open('weather.json', 'r')
    weatherData = json.load(file)
    return weatherData
