import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"

account_sid = os.environ.get("AUTH_SID")
auth_token = os.environ.get("AUTH_TOKEN")

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

parameters={
    "lat": 19.1238,
    "lon": 72.9126,
    "appid":os.environ.get("OWM_API_KEY"),
    "cnt":4
}
response=requests.get(url=OWM_Endpoint,params=parameters)
response.raise_for_status()
weather_data=response.json()
weather_list=weather_data["list"]
bring_umbrella=False
for i in weather_list:
    if i["weather"][0]["id"]<700:
        bring_umbrella=True
if bring_umbrella:
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="Bring Umbrella.",
        from_="+13612215192",
        to="+91 70426 41180",
    )
    print(message.status)
