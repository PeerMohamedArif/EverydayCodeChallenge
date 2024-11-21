import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


OWM_endpoint=""
api_key= ""
weather_params={
    "lat":-3.386925,
    "lon":36.682995,
    "appid":api_key,
    "cnt": 4

}



will_rain= False
response=requests.get(url=OWM_endpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()
#print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code=(hour_data["weather"][0]["id"])
    if int(condition_code)<700:
        will_rain=True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies={"https": os.environ['https_proxy']}
    client = Client(account_sid, auth_token,http_client=proxy_client)
    message = client.messages.create(
        body="Rain Alert,Its going to rain today ,Be sure to take an umbrella",
        from_="",
        to="",
    )

    print(message.status)
