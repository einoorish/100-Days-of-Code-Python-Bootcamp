from turtle import Turtle, Screen


def challenge2():
    # draw a dashed line

    arrow = Turtle()

    for i in range(0, 8):
        arrow.forward(8)
        arrow.penup()
        arrow.forward(8)
        arrow.pendown()


challenge2()

screen = Screen()
screen.exitonclick()
