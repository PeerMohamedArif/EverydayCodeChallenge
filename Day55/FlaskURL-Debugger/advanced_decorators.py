class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in=False

def authenticated_decorater(function):
    def wrapper_function(*args,**kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper_function

@authenticated_decorater
def create_blog_post(user):
    print(f"This is {user.name} 's blog")


user1=User("Arif")
user1.is_logged_in=True
create_blog_post(user1)
