import requests

response1=requests.get(url="http://api.open-notify.org/is-now.json")
print(response1.status_code)
if response1.status_code==404:
    raise Exception("That resource does not exist")
elif response1.status_code==401:
    raise Exception("You are not authorised to access this data.")

response1.raise_for_status()
