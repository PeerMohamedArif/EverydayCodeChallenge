from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5,stretch_wid=0.5) # already its 20x20 now it will be 10x10
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x,random_y)



