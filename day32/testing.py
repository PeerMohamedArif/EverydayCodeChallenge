import smtplib
import datetime as dt

# my_email = "example@gmail.com" # your mail
# my_password = "abcd1234" # your pw

# # Create your connection
# # Make sure you've got the correct smtp address for your email provider
# connection = smtplib.SMTP("smtp.gmail.com") 
# # Secure our connection
# connection.starttls() # transport layer security
# # Login
# connection.login(user=my_email, password=my_password)
# # Send the email
# connection.sendmail(
#     from_addr=my_email, 
#     to_addrs="msgreciever@gmail.com", 
#     msg="Subject:Hello There\n\nThis is the body of the email.")
# # Close the connection
# connection.close()

# ## Alternatively
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="msgreciever@gmail.com", 
#         msg="Subject:Hello Again\n\nThis is the body of the email.")

# ------------------- DATETIME MODULE --------------------#
now = dt.datetime.now()
year = now.year
day_of_the_week = now.weekday()
print(now, type(now)) # type of now is datetime.datetime
print(year, type(year)) # type of year is int
print(day_of_the_week, type(day_of_the_week)) # type of day_of_the_week is int
# Monday -> 0, Tuesday -> 1, Wednesday -> 2 and so on

date_of_birth = dt.datetime(year=2023, month=6, day=11)
print(date_of_birth)
