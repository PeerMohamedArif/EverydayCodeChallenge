from turtle import Screen,Turtle
from paddle import Paddle
from balll import Ball
from score import ScoreBoard
import time

is_game_on=True
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=ScoreBoard()


screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collision detection with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #collision with r_paddle
    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320) :
        ball.bounce_x()

    # detect miss of paddle
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()







screen.exitonclick()
