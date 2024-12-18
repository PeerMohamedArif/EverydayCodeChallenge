from flask import Flask
import random
app=Flask(__name__)

#print(random.__name__)
print(__name__)


# what is this syntax about @app.route('/')? its a python decorator, in advanced python projects
# decorator function gives additional functionality to an existing function
# normal functions are basically first class objects
# the () in a function is the activator of the function
# in simple words you can pass a function as a argument to a object or as a argument to some other function without ()
# or even return it without ()
# but when you want to call the function you can use the ()

@app.route('/')# home page that /
def hello_world():
    return 'Hello, World! '

@app.route("/bye")
def say_bye():
    return "Bye!"

if __name__ == '__main__':
    app.run()

# In Python, the special name __main__ is used for two important constructs:
# 1.) the name of the top-level environment of the program, which can be checked using the __name__ == '__main__' expression; and
# 2.) the __main__.py file in Python packages.

# if __name__ == '__main__':
#     # Execute when the module is not initialized from an import statement.
#     ...
