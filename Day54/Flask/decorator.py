import time

def delay_decorator(function):
    def wrapper_function():
        # decorator function(outer function) is a function the wraps a function and gives that function some additional
        # functionality
        time.sleep(3)
        # you can do something before before the actual call
        function()
        # you can do something after the call as well
    return wrapper_function

@delay_decorator #
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("bye")

def say_greeting():
    print("how are you")

say_greeting()# triggers immediately
say_hello()# triggers after the sleep

# same as above with a different form of syntax
# decorated_function=delay_decorator(say_greeting())
# decorated_function()
