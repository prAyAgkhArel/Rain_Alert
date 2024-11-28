

# MY_LAT = 26.795306
# MY_LON = 87.290393
MY_LAT = 48.545460
MY_LON = -71.659309

import requests
import os
from twilio.rest import Client


weather_api_key = os.getenv("WEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
phone_number = os.getenv("MY_PHONE_NUMBER")


trial_number = "+16812305718"


weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast?cnt=4"
parameters ={
    "lat" : MY_LAT,
    "lon" : MY_LON,
    "appid": weather_api_key,

}

#weather_endpoint = f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LAT}&lon=-{MY_LON}&cnt=3&appid={API_KEY}"
response = requests.get(url=weather_endpoint, params=parameters)

response.raise_for_status()
weather_data = response.json()

will_rain = False
for timestamps in weather_data["list"]:
    id = timestamps["weather"][0]["id"]
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Carry Umbrella☂️",
        from_=trial_number,
        to=phone_number,
    )

    print(message.status)   # sends the message to the twilo verified number from the twilo generated number





