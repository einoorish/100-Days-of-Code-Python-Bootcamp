from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.x_pos = x_pos
        self.goto(x_pos, 0)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 40
            self.goto(self.x_pos, new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 40
            self.goto(self.x_pos, new_y)
