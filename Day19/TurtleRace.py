from random import random
from turtle import *
import turtle as t
import random
colors=["violet","indigo","blue","green","yellow","orange","red"]
is_race=False
y_positions=[-150,-100,-50,0,50,100,150]
screen=Screen()
screen.setup(500,400)
user=screen.textinput( "Turtle race", "Which Turtle will win the race, Choose a color")
all_turtles=[]


for turtle_ind in range(0,7):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_ind])
    new_turtle.goto(x=-235, y=y_positions[turtle_ind])
    all_turtles.append(new_turtle)

if user:
    is_race=True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race=False
            winning_turtle=turtle.pencolor()
            if winning_turtle==user:
                print(f"Congratulations, Your {winning_turtle} turtle has won")

            else:
                print(f"Sorry, you Lose,The {winning_turtle} turtle is the winner")

        random_speed=random.randint(0,10)# inclusive from 0 to 10
        turtle.forward(random_speed)

screen.exitonclick()
