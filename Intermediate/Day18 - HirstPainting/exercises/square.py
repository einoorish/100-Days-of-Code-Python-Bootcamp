from turtle import Turtle, Screen


def challenge1():
    # draw a square

    arrow = Turtle()

    arrow.forward(100)
    arrow.right(90)
    arrow.forward(100)
    arrow.right(90)
    arrow.forward(100)
    arrow.right(90)
    arrow.forward(100)


challenge1()


# our window won't disappear(program will keep running) until we click on it
screen = Screen()
screen.exitonclick()
