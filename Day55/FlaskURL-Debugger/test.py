from flask import Flask

app=Flask(__name__)
@app.route('/')# home page that /
def hello_world():
    return 'Hello, World! '



# ---------------------------------------###------------------------------------------------------------------------
# rendering html tag elements with flask

# you can use html tags in return
# the tags can be of any type even an img src
# suppose if the line goes too big, inside the tag quotation mark just hit enter
# will automatically create a line.

@app.route("/bye")
def say_bye():
    return ("<h1><b>Bye!</b>"
            "</h1><img src='https://media.istockphoto.com/id/175009379/photo/giant-panda-bear-eating-bamboo.jpg?s=612x612&w=0&k=20&c=EYUlXKzjxe23OSXHO9jlugQhH_VWtF1-2NUaOSXsijA='>")


# ---------------------------------------###------------------------------------------------------------------------
# variables in flask

# it can also be /username/<name> which catches the variable/ 1 where the 1 page will
# return the same output
# if you go to the local host and use the url the <> will become a variable as you mention in
# the url  http://127.0.0.1:5000/username/arif will return hello arif

# for example  @app.route("/username/<name>/1")

# the name in the variable has to be the same suppose lets say in Decorator function we have <username> instead of
# name it will return an error in the webpage and not in console

# for example @app.route("/username/<username>/1")  # because the function has name


# ---------------------------------------###------------------------------------------------------------------------
# converters in flask

#  what is <converter : variable name>  basically converts any datatype you specify if you give string
#  converts the value to a string -accepts any text without a slash
#  for example <string: name >   (also includes the slash)
# if you want slash because its a path you can use
# <path : name > for the above greet example / is included

# ---------- Converter Types ----------#
# string: (default) accepts any text without a slash
# int: accepts positive integers
# float: accepts positive floating point values
# path: like string but also accepts slashes
# uuid: accepts UUID strings


@app.route("/username/<path:name>/1") # here converter is path
def greet(name):
    return f"Hello {name}"


# ---------------------------------------###------------------------------------------------------------------------
# debug in flask

# instead of stopping and running the server everytime you can set debug mode to on
# debug mode will help in identifying the error
# you can also use flask debugger for which the pin is required

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)


