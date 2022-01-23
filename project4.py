#!/usr/bin/env python3

from os import kill
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("980x900")
root.title("Temperature Conversion")

# USER INPUT

label = Label(
    root,
    text="Temperature in Celsius: ",
    font=("Times", 18, "bold"),
    fg="#00FFFF",
    justify=("right"),
)
tc_string = StringVar()
label.place(x=50, y=25, width=200, height=30)
tc_entry = Entry(root, textvariable=tc_string, font=("Times", 18))
tc_entry.place(x=250, y=25, width=200, height=30)


# OUTPUT IN FAHRENHEIT


# FUNCTIONS


def convert():

    # Celsius to Fahrenheit Formula: (°C * 1.8) + 32 = °F

    # Fahrenheit to Celsius Formula: (°F - 32) / 1.8 = °C

    # def clear():
    #   mi_string.set("")
    #   yl_string.set("")
    #   yfv_string.set("")

    def kill():
        root.destroy


c2f = Button(root, text="Convert C to F, command=convert", font=("Times", 12, "bold"))
c2f.place(x=25, y=200, width=150, height=30)

# clear = Button(root, text="Clear", command=clear, font=("Times", 12, "bold"))
# clear.place(x=225, y=200, width=150, height=30)

exit = Button(root, text="Exit", command=kill, font=("Times", 12, "bold"))
exit.place(x=425, y=200, width=150, height=30)

root.mainloop()


# the main conversion
# window configuration
# user instruction and input
# shows result for opposite temp
# allow button to be clicked to convert
# add function for the button to convert from C to F
# bonus points for code to catch user input error
