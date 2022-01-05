from flask import Flask
import json, requests

app = Flask(__name__)



@app.route('/get/Weather' , methods = ['GET'])
def getWeather():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=mangalore&appid=f5990901916de44b03db0a2d1c42140d'
    response = requests.get(url)
    response.raise_for_status()
    weatherData = json.loads(response.text)
    return weatherData

    
    

if __name__ == "__main__":
    app.run(debug=True)