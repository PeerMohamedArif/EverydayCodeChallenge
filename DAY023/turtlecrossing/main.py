import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car=CarManager()
player=Player()
screen.listen()
score=Scoreboard()
screen.onkeypress(player.move_forward,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for cars in car.all_cars:
        if cars.distance(player)<20:
            game_is_on=False
            score.game_over()
    # detect cross success
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        score.increase_level()


screen.exitonclick()
