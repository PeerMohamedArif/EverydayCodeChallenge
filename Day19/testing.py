from turtle import *
import turtle as t

teddy=Turtle()
screen=Screen()
def move_forward():
    teddy.fd(10)



screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()
