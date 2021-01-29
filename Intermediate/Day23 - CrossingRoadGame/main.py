import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=500)
screen.colormode(255)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "space")

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if counter == 6:
        car_manager.generate_new_car()
        counter = 0

    car_manager.move_cars()

    if player.has_reached_finish_line():
        scoreboard.increment_score()
        player.reset_player()

    if car_manager.detect_collision_with_turtle(player.pos()):
        turtle = Turtle()
        turtle.write("GAME OVER", align="center", font=("Courier", 18, "bold"))
        game_is_on = False

    counter += 1


screen.exitonclick()