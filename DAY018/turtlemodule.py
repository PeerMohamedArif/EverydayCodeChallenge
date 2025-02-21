import random
from turtle import *
import turtle
import heroes
from turtle import Turtle as T, Screen as S
print(heroes.gen())


rocky=Turtle()
rocky.shape("turtle")
rocky.color("red")
for i in range(4):
    rocky.forward(100)
    rocky.right(90)


tommy = T()
tommy.shape("triangle")
tommy.color("blue")
for _ in range(15):
    tommy.forward(10)
    tommy.pendown()
    tommy.forward(10)
    tommy.penup()


ronny= Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink", "brown", "grey", "violet"]
for n in range(3, 11):
    ronny.color(random.choice(colors))
    angle = 360/n
    for _ in range(n):
        ronny.forward(100)
        ronny.right(angle)


teddy = turtle.Turtle()
turtle.colormode(255)
directions = [0, 90, 180, 270]
teddy.width(5) # you can use pensize() as well
teddy.speed("fastest")
def decide_color_for_teddy():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple
def random_walk(n):
    for _ in range(n):
        teddy.color(decide_color_for_teddy())#you can use pencolor()
        teddy.forward(20)
        teddy.setheading(random.choice(directions))
random_walk(300)


randy = turtle.Turtle()
turtle.colormode(255)
randy.speed("fastest")
def decide_color_for_randy():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        randy.color(decide_color_for_randy())
        randy.circle(100)
        randy.setheading(randy.heading() + 10)


draw_spirograph(5)

screen= Screen()
screen.exitonclick()
