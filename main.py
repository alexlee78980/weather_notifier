import requests
import os
from twilio.rest import Client

#free accounts so dont need to encrypt
account_sid = "AC3dc2b8fa0586bf79feb8376dd0b4cf48"
auth_token = "2e72d8441686e39e72d66c9968cc7489"
weather_params = {
    "lat": 49.2497,
    "lon": -123.1193,
    "exclude": "currently,daily,minutely",
    "appid": "20739fb2addf15292a66f0d9d0a0f3a5"
}
res = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
res.raise_for_status()
hourly_weather = res.json()["hourly"]

for weather in hourly_weather[:13]:
    if weather["weather"][0]["id"] < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body='It will rain today, bring an umbrella!',
            from_="+12242617722",
            to='+1 778 512 6634'
        )
        print(message.status)
        break
