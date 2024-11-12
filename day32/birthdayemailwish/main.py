import smtplib as smtp
import datetime as dt
import pandas as pd
import random


my_email= "example@gmail.com"
my_password="_________________"

birthday_dict=pd.read_csv("birthdays.csv").to_dict(orient="records")

for birthday in birthday_dict:
    if(dt.datetime.now().month,dt.datetime.now().day)==(birthday["month"],birthday["day"]):
        file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"

        with open (file_path) as letter_file:
            contents=letter_file.read()
            contents=contents.replace("[NAME]",birthday["name"])

        with smtp.SMTP("smtp.gmail.com", port= 587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday["email"],
                                msg=f"Subject: Happy Birthday!!!\n\n{contents}"
                                )

