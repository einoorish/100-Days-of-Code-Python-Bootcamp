from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


# to avoid showing paddle moving to its initial position
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() == 340:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() == -340:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() == 380:
        ball.reset_ball()
        scoreboard.l_increment_score()
    elif ball.xcor() == -380:
        ball.reset_ball()
        scoreboard.r_increment_score()


screen.exitonclick()
