from flask import render_template
from flask import Flask,request
import requests
import smtplib

posts=requests.get(url="your endpoint").json()
OWN_EMAIL="your email"
OWN_PASSWORD="______________"

app=Flask(__name__)
@app.route('/')
def  get_all_posts():
    return render_template("index.html",all_posts=posts)
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        # print(data)
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html",  msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
# @app.route('/form-entry', methods=["POST"])
# def receive_data():
#     print(request.form['name'])
#     print(request.form['email'])
#     print(request.form['phone'])
#     print(request.form['message'])
#
#     return "<h1>Successfully Submitted</h1>"

def send_email(name,email,phone,message):
    email_message = f"Subject: New Message\nFrom: {email}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user = OWN_EMAIL, password = OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__=="__main__":
    app.run(debug=True,port=5001)
