from turtle import Turtle

FONT = ("Courier", 50, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")

        self.l_score = 0
        self.r_score = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_increment_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_increment_score(self):
        self.r_score += 1
        self.update_scoreboard()
