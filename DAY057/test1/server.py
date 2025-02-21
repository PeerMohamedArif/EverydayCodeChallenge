from flask import Flask
from flask import render_template
import random
import datetime as dt
import requests

app=Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year=dt.datetime.now().year
    return render_template("index.html",num=random_number,year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url=f"https://api.genderize.io?name={name}"
    age_url=f"https://api.agify.io?name={name}"
    gender_response=requests.get(url=gender_url)
    print(gender_response.raise_for_status())
    age_response=requests.get(url=age_url)
    print(age_response.raise_for_status())
    gender_data=gender_response.json()
    age_data=age_response.json()
    gender=gender_data['gender']
    age=age_data['age']
    return render_template("guess.html",person_name=name,person_gender=gender,person_age=age)


if __name__== "__main__":
    app.run(debug=True, port=5001)
