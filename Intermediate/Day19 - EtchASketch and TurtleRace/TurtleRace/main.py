import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=-70 + (30 * i))
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        # 230 = end of window - turtle width/2
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()

            if winner == user_bet:
                print("You've won!")
            else:
                print(f"You've lost. The {winner} is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
