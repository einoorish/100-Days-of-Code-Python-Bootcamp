import random
from turtle import Turtle, Screen


def challenge3():
    # draw a triangle, square, pentagon.... decagon - each with a random color

    arrow = Turtle()

    for sides_num in range(3, 11):
        # select random color:
        r = random.random()
        g = random.random()
        b = random.random()

        arrow.color(r, g, b)

        # calculate angle and draw the shape:
        angle = 360/sides_num

        for side in range(0, sides_num):
            arrow.forward(100)
            arrow.right(angle)


challenge3()

screen = Screen()
screen.exitonclick()
