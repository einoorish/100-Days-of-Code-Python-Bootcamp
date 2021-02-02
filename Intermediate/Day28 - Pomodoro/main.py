from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✅"

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    global timer
    reps = 0
    window.after_cancel(timer)

    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    if reps % 2 == 0:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    elif reps < 7:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
        reps = 0
        return


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def add_check_mark(work_sessions):
    marks = []
    for _ in range(work_sessions):
        marks.append(CHECK_MARK)
    check_marks.config(text=marks)


def count_down(seconds):
    formatted_min = math.floor(seconds / 60)
    formatted_sec = seconds % 60
    if formatted_sec < 10:
        formatted_sec = f"0{formatted_sec}"

    canvas.itemconfig(timer_text, text=f"{formatted_min}:{formatted_sec}")
    if seconds > 0:
        global timer
        timer = window.after(1000, count_down, seconds - 1)
    else:
        global reps
        reps += 1

        if reps % 2 == 0:
            add_check_mark(math.floor(reps / 2))

        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12))
check_marks.grid(row=3, column=1)

window.mainloop()
