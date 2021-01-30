import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_guesses = 0
mistakes = []

while correct_guesses < 50:

    answer_state = screen.textinput(title=f"{correct_guesses}/50 States Guessed", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    data = pandas.read_csv("50_states.csv")

    data_frame = data[data["state"] == answer_state]
    if not data_frame.empty:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data_frame.x), int(data_frame.y))
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))
        correct_guesses += 1
    else: mistakes.append(answer_state)

data_dict = {
    "Mistakes": mistakes,
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("states_to_learn.csv")

