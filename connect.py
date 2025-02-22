from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_openweather_api_key"  # Replace with your OpenWeatherMap API Key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        if city:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric'  # Fetch temperature in Celsius
            }
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'error': 'City not found'}
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
