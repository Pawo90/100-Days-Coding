import math
from datetime import datetime
import requests
from calculations import calc
import time
import smtplib

ISS_API = "http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_API = "https://api.sunrise-sunset.org/json"

MY_EMAIL = "pl.pawel.pieta@gmail.com"
MY_PASSWORD = "kaerbstuviwofbdm"
MY_LATITUDE = 50.064651
MY_LONGITUDE = 19.944981
Re = 6371.0
H = 412

parameters = {
    'lat': MY_LATITUDE,
    'lng': MY_LONGITUDE,
    'formatted': 0
}


# TODO 1: Request for current ISS position on the sky
def request_iss_position(api_endpoint, *args):
    response = requests.get(api_endpoint, params=args[0])
    response.raise_for_status()
    return response.json()


def is_iss_overhead(iss_loc_data, my_lat, my_lon):
    if my_lat - 5 <= float(iss_loc_data['latitude']) <= my_lat + 5 and \
       my_lon - 5 <= float(iss_loc_data['longitude']) <= my_lon + 5:
        return True


# REQUEST FOR ISS POSITION ---------------------------
data = request_iss_position(ISS_API, None)
iss_loc_data = data['iss_position']
print(iss_loc_data)

# TODO 2.1: Request for sunrise and sunset
# REQUEST FOR CURRENT DATA ---------------------------
data = request_iss_position(SUNRISE_SUNSET_API, parameters)
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

now = datetime.now()
current_loc_data = {'longitude': MY_LONGITUDE,
                    'latitude': MY_LATITUDE,
                    'now': now.hour,
                    'sunrise': sunrise,
                    'sunset': sunset
                    }
print(current_loc_data)

calc(current_loc_data['latitude'], current_loc_data['longitude'],
     iss_loc_data['latitude'], iss_loc_data['longitude'])

# TODO 2.2: Check if in current location is after sunset
if current_loc_data['now'] > current_loc_data['sunset'] or current_loc_data['now'] < current_loc_data['sunrise']:
    if is_iss_overhead(iss_loc_data, MY_LATITUDE, MY_LONGITUDE):
        print("Look up!")
    else:
        print("ISS is to far away")


# TODO 3: Send a email
def send_email():
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: ISS IS OVERHEAD\n\nLook Up!")


# TODO 4: RUN the code every 60 sec
