from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0# name constants like this in caps
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head= self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS :
            self.add_segment(position)
    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[segment_num - 1].xcor()
            new_y_cor = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x_cor, new_y_cor)
        self.segments[0].forward(MOVE_DISTANCE)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
