from flask import Flask, request
import json, requests

app = Flask(__name__)

# function to convert kelvin to celsius
def convertToCelsius(kelvin):
    return round(kelvin - 273.15, 2)

@app.route('/weather' , methods = ['GET'])
def getWeather():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=mangalore&appid=f5990901916de44b03db0a2d1c42140d'
    response = requests.get(url)
    response.raise_for_status()
    weatherData = json.loads(response.text)
    dataToSend = {
        'temp': convertToCelsius(weatherData['main']['temp']),
        'feels_like': convertToCelsius(weatherData['main']['feels_like']),
        'humidity': weatherData['main']['humidity'],
        'description': weatherData['weather'][0]['description'],
        'wind_speed': weatherData['wind']['speed']
    }
    return json.dumps(dataToSend)

@app.route('/emailvalidate' , methods = ['GET'])
def getEmailValidate():
    email = request.args.get('email')
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email}
    )
    status = response.json()['status']
    if status == "valid":
        return {"response": True}
    elif status == "invalid":
        return {"error": "Please enter a valid email address!"}
    else:
        return {"error": "Please enter a valid email address!"}

if __name__ == "__main__":
    app.run(debug=True)