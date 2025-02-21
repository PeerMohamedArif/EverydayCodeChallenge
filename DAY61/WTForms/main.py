from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired ,Length , Email

'''
On MacOS type:
pip install -r requirements.txt
'''
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length( max=100), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length( min=8 , max=50)])
    submit= SubmitField(label="Log in")

app = Flask(__name__)

app.secret_key = "helloworld"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST','GET'])
def login():
    login_form=LoginForm()
    login_form.validate_on_submit()
    if request.method=="POST" and login_form.validate():
        email=login_form.email.data
        password=login_form.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html", form=login_form)
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
