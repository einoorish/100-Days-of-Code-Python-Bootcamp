from turtle import Turtle, Screen


def challenge5():
    # draw a spirograph
    circle = Turtle()
    circle.speed("fastest")
    circle.circle(100)

    for _ in range(0, 36):
        circle.left(10)
        circle.circle(100)


challenge5()

# our window won't disappear(program will keep running) until we click on it
screen = Screen()
screen.exitonclick()
