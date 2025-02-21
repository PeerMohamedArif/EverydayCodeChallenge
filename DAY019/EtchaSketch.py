from turtle import *
import turtle as t

teddy=Turtle()
screen=Screen()

def move_forward():
    teddy.forward(20)
def move_reverse():
    teddy.backward(20)
def move_left():
    teddy.left(20)
def move_right():
    teddy.right(20)
def clear_screen():
    teddy.clear()
    teddy.penup()
    teddy.home()
    teddy.pendown()

screen.listen()
screen.onkeypress(key="w",fun=move_forward)
screen.onkeypress(key="s",fun=move_reverse)
screen.onkeypress(key="a",fun=move_left)
screen.onkeypress(key="d",fun=move_right)
screen.onkey(key="c",fun=clear_screen)
screen.exitonclick()
