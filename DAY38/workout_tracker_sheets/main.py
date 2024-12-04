import requests
from datetime import datetime
import os
GENDER="male"
WEIGHT=85
HEIGHT=183
AGE=26
APP_ID=os.getenv("APP_ID")
API_KEY=os.getenv("API_KEY")

exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint=os.getenv("sheety_endpoint")
sheety_token=os.getenv("sheety_token")

exercise_text=input("what workout did you do")
headers={
    "x-app-id": APP_ID,
    "x-app-key":API_KEY
}
parameters={
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE,

}
response=requests.post(url=exercise_endpoint,json=parameters,headers=headers)
result=response.json()
#print(result)

today_date=datetime.now().strftime("%d/%m/%Y")
now_time=datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {  # Replace 'sheet1' with your actual tab name if different
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_headers={
        "Authorization": f"Bearer {sheety_token}",
    }
    sheet_response=requests.post(url=sheety_endpoint,json=sheet_inputs,headers=sheety_headers)
    print(sheet_response.text)
