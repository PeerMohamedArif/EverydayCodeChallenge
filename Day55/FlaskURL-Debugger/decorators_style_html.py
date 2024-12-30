from flask import Flask

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<i>{function()}</i>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function

app=Flask(__name__)
@app.route('/')# home page that /
def hello_world():
    return 'Hello, World! '

# @app.route("/bye")
# def say_bye():
#     return "<u><em><b>Bye!</b></em></u>" # prone to errors

@app.route("/bye")
@make_underlined
@make_emphasis
@make_bold
def say_bye():
    return "Bye!" # this will return bold italic underlined bye

# it can also be /username/<name> which catches the variable/ 1 where the 1 page will
# return the same output
@app.route("/username/<path:name>/1")
def greet(name):
    return f"Hello {name}"

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)
