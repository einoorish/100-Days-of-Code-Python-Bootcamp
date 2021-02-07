import json
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

def show_nothing_found_message():
    messagebox.showinfo(title="Opps", message="Nothing Found. ")


def show_data(data):
    website = data
    username = data["username"]
    password = data["password"]
    messagebox.showinfo(title="website", message=f"Username/Email: {username}\nPassword: {password}")


def search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        show_nothing_found_message()
    else:
        try:
            match = data[website_entry.get()]
        except KeyError:
            show_nothing_found_message()
        else:
            show_data(match)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def retrieve_new_dictionary_entry():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please make sure you haven't left any fields empty")
        return None
    else:
        return {
            website: {
                "username": username,
                "password": password
            }
        }


def save_data():
    new_entry = retrieve_new_dictionary_entry()

    if new_entry is not None:
        is_ok = messagebox.askokcancel(title=new_entry, message=f"Are you sure entered data is correct?")

        if is_ok:

            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_entry, file, indent=4)
            else:
                data.update(new_entry)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
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

website_entry = Entry(width=21)
username_entry = Entry(width=35)
password_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="EW")
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry.grid(row=3, column=1, sticky="EW")

search_button = Button(text="Search", command=search)
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=save_data)
search_button.grid(row=1, column=2, sticky="EW")
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
