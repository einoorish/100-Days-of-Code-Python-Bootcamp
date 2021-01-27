from turtle import Turtle, write

FONT = font=("Arial", 18, "normal")

class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.value = 0

        self.hideturtle()
        self.penup()
        self.goto(0, 200)

        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.value}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)

    def increment_score(self):
        self.value += 1
        self.update_score()
