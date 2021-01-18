from turtle import Screen, Turtle
from random import choice
import colorgram

rgb_colors = []


def get_colors_from_painting():
    colors = colorgram.extract("hirst_painting.jpg", 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        new_color = (r, g, b)
        print(new_color)
        rgb_colors.append(new_color)


dot = Turtle()
dot.penup()
dot.hideturtle()
dot.speed("fastest")

get_colors_from_painting()

screen = Screen()
screen.colormode(255)

# move to the staring position
dot.setheading(220)
dot.forward(6*50)

# reset heading
dot.setheading(0)


for _ in range(10):

    for _ in range(10):
        dot.dot(20, choice(rgb_colors))
        dot.forward(50)

    # face up
    dot.setheading(90)
    dot.forward(50)
    # face left
    dot.setheading(180)
    # move to the beginning of line
    dot.forward(500)
    # face right
    dot.setheading(0)

screen.exitonclick()