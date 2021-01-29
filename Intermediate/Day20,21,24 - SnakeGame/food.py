from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.penup()

        self.shape("circle")
        self.shapesize(0.7, 0.7)
        self.color("green")

        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(-230, 230)
        random_y = randint(-230, 230)
        self.goto(random_x, random_y)
