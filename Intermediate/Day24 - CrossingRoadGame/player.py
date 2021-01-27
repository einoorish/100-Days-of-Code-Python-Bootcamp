from turtle import Turtle

STARTING_POSITION = (0, -220)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 220


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reset_player()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def has_reached_finish_line(self):
        return self.ycor() == FINISH_LINE_Y
