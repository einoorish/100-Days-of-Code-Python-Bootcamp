from turtle import Turtle, write

FONT = font = ("Arial", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.penup()
        self.goto(0, 200)

        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over", align="center", font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_score()
