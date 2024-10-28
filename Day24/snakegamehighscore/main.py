from turtle import Screen
from scoreboardFILES import ScoreBoard
from snakeFiles import Snake
from food import Food
import time

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Expanding Snake")
screen.tracer(0)

snake=Snake()
food=Food()
score=ScoreBoard()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_start= True
while game_start:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-290 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            score.reset()
            snake.reset()

screen.exitonclick()

