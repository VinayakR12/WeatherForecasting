from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("DATA_ENDPOINT")
Forecast_URL = os.getenv("DATA_FORECAST")
AIR_URL=os.getenv("DATA_AIR")

CITIES = {
    "Mumbai": {"lat": 19.076, "lon": 72.8777},
    "Pune": {"lat": 18.5204, "lon": 73.8567},
    "Kolhapur": {"lat": 16.704, "lon": 74.2433},
    "Satara": {"lat": 17.685, "lon": 74.003},
    "Sangli": {"lat": 16.8524, "lon": 74.5815},
}

# Route to fetch current weather
def get_weather(city):
    lat, lon = CITIES[city]["lat"], CITIES[city]["lon"]
    url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Route for 5-day weather forecast
def get_forecast(city):
    lat, lon = CITIES[city]["lat"], CITIES[city]["lon"]
    url = f"{Forecast_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Route for air pollution data
def get_air_quality(city):
    lat, lon = CITIES[city]["lat"], CITIES[city]["lon"]
    url = f"{AIR_URL}?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city", "Mumbai")
    data = get_weather(city)
    return jsonify(data)

@app.route("/forecast", methods=["GET"])
def forecast():
    city = request.args.get("city", "Mumbai")
    data = get_forecast(city)
    return jsonify(data)

@app.route("/air_quality", methods=["GET"])
def air_quality():
    city = request.args.get("city", "Mumbai")
    data = get_air_quality(city)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

