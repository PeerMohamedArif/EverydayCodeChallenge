from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     # our HTML should be in the templates folder for this to work
#     return render_template("index.html")

# @app.route('/')
# def home():
#     # our HTML should be in the templates folder for this to work
#     return render_template("index1.html")

# @app.route('/')
# def angela_cv():
#     # static files such as CSS, Javascript and images have to be kept in the static folder
#     return render_template("Angela.html")

if __name__ == "__main__":
    app.run(debug=True)
