import requests
from datetime import datetime
my_lat=13.082680
my_lng=80.270721

parameters={
    "lat":my_lat,
    "lng":my_lng,
    "formatted":0,
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now=datetime.now()

print(time_now.hour)
