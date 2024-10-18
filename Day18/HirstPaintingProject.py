# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# #print(colors)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#print(rgb_colors)
from turtle import *
import turtle as t
import turtle
import random
number_of_dots=100
teddy= t.Turtle()
teddy.speed("fastest")
teddy.penup()
teddy.hideturtle()
color_list=[(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
            (138, 31, 20),(134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
            (232, 176, 165),(160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
            (82, 148, 129),(147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)

step=50
teddy.setheading(225)
teddy.forward(300)
teddy.setheading(0)


for dots in range(1,number_of_dots+1):
    teddy.dot(20,random.choice(color_list))
    teddy.fd(step)

    if dots%10==0:
        teddy.setheading(90)
        teddy.fd(step)
        teddy.setheading(180)
        teddy.fd(500)
        teddy.setheading(0)



screen=t.Screen()
screen.exitonclick()




