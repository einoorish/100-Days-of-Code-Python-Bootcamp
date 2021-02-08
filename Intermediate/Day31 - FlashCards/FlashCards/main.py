from tkinter import *
import random
import pandas

INITIAL_DATA_PATH = "data/de_to_en.csv"
WORDS_TO_LEARN_PATH = "data/words_to_learn.csv"
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

current_word = {}
to_learn = {}

try:
    data_frame = pandas.read_csv(WORDS_TO_LEARN_PATH)
except FileNotFoundError:
    original_data = pandas.read_csv(INITIAL_DATA_PATH)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_frame.to_dict(orient="records")


def flip_card():
    card.itemconfig(language_label, text="English", fill="white")
    card.itemconfig(word_label, text=current_word["English"], fill="white")
    card.itemconfig(card_background, image=card_back_image)


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    card.itemconfig(language_label, text="German", fill="black")
    card.itemconfig(word_label, text=current_word["German"], fill="black")
    card.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv(WORDS_TO_LEARN_PATH, index=False)
    next_card()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# load images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = card.create_image(400, 263, image=card_front_image)
language_label = card.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_label = card.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

card.grid(row=0, column=0, columnspan=2, sticky="EW")

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
next_card()

mainloop()
