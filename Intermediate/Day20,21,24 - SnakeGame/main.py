from turtle import Turtle, Screen
from time import sleep

from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.tracer(0)  # to remove animation
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True

while game_is_on:
    sleep(0.1)  # to slower the snake
    snake.move()

    screen.update()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increment_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
