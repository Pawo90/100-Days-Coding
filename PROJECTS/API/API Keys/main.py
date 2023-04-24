# API Endpoint: https://home.openweathermap.org/
# Example: https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
# API My Key "Default": cdc2233a60c23418c0c308b30cfe8851
# API My Key "Python": 35c937ccdbf4296994285341a0f8bc77


# https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=35c937ccdbf4296994285341a0f8bc77

import requests

# Current Localisation Latitude and Longitude
MY_LATITUDE = 50.049683
MY_LONGITUDE = 19.944544
API_KEY = "35c937ccdbf4296994285341a0f8bc77"

api_endpoint = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(api_endpoint, params=parameters)
# print(response.status_code)
response.raise_for_status()
# save data in JSON format
weather_data = response.json()
# slice data
weather_slice = weather_data['hourly'][:12]

# Check if it's gonna rain:
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    # Condition codes
    # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

