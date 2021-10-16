from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        city_name = request.form['city']
        api_key = "your_api_key"

        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric')

        weather_data = weather_url.json()

        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        clouds = weather_data['clouds']['all']

        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city_name)

    return render_template("layout.html")

app.run(debug=True)