from tkinter import *

window = Tk()
window.title("Converter")
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)
label_km = Label(text="Km")
label_km.grid(row=1, column=2)

label_equal = Label(text="is equal to ")
label_equal .grid(row=1, column=0)

label_km_value = Label(text="0")
label_km_value.grid(row=1, column=1)


def calculate():
    miles = int(entry.get())
    km = miles * 1.609
    label_km_value.config(text=f"{km}")


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

mainloop()