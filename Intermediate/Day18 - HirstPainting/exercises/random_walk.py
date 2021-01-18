from turtle import Turtle, Screen


def random_color():
    # returns a tuple representing a random color
    r = random.random()
    g = random.random()
    b = random.random()

    color = (r, g, b)
    return color


def challenge4():
    arrow = Turtle()

    arrow.pensize(8)
    arrow.forward(16)

    arrow.speed("fastest")

    for _ in range(0, 150):
        arrow.color(random_color())
        arrow.forward(16)
        arrow.setheading(90*random.randint(0, 4))


challenge4()

screen = Screen()
screen.exitonclick()
