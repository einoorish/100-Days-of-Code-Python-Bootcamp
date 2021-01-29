import time
from turtle import Turtle

INITIAL_MOVE_SPEED = 0.1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.y_direction = 1
        self.x_direction = 1
        self.move_speed = INITIAL_MOVE_SPEED
        self.penup()

    def move(self):
        new_x = self.xcor() + 10 * self.x_direction
        new_y = self.ycor() + 10 * self.y_direction
        self.goto(new_x, new_y)

    def reset_ball(self):
        time.sleep(1)
        self.home()
        self.move_speed = INITIAL_MOVE_SPEED
        self.x_direction = -self.x_direction

    def bounce_y(self):
        self.y_direction = -self.y_direction

    def bounce_x(self):
        self.x_direction = -self.x_direction
        self.move_speed *= 0.9
