from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(2, 5)
    nr_symbols = random.randint(1, 2)
    nr_numbers = random.randint(2, 5)

    password_list = []

    for i in range(0, nr_letters):
        password_list.append(random.choice(letters))

    for i in range(0, nr_symbols):
        password_list.append(random.choice(symbols))

    for i in range(0, nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
    pyperclip.paste()


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Are you sure entered data is correct?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")

            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
username_entry = Entry(width=35)
password_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry.grid(row=3, column=1, sticky="EW")

generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=save_data)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
