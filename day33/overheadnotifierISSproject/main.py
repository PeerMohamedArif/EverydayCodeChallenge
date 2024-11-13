import requests
from datetime import datetime
import smtplib
import time

my_email=""
password=""
my_lat=13.082680
my_lng=80.270721

def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data=response.json()

    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude=float(data["iss_position"]["latitude"])

    if my_lat-5<=iss_latitude<=my_lat+5 and my_lng-5<=iss_longitude<=my_lng+5:
        return True

def is_night():
    parameters={
        "lat":my_lat,
        "lng":my_lng,
        "formatted":0,
    }
    response1=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response1.raise_for_status()
    data1=response1.json()
    sunrise=int(data1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data1["results"]["sunset"].split("T")[1].split(":")[0])

    time_now=datetime.now().hour
    if time_now>= sunset or time_now<= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: Look Up\n\n The ISS is above you in the sky"
                            )
