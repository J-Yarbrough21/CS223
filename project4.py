#!/usr/bin/env python3

from os import kill
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("700x300")
root.title("Temperature Conversion")

# USER INPUT

label = Label(
    root,
    text="Temperature in Celsius: ",
    font=("Times", 18, "bold"),
    justify=("right"),
)
tc_string = StringVar()
label.place(x=155, y=50, width=200, height=30)
tc_entry = Entry(root, textvariable=tc_string, font=("Times", 18, "bold"))
tc_entry.place(x=350, y=50, width=200, height=30)

# OUTPUT IN FAHRENHEIT

label = Label(
    root,
    text=" Temperature in Fahrenheit:  ",
    font=("Times", 18, "bold"),
    justify=("right"),
)
tf_string = StringVar()
label.place(x=115, y=125, width=250, height=30)
tf_entry = Entry(root, textvariable=tf_string, font=("Times", 18))
tf_entry.place(x=350, y=125, width=200, height=30)


# FUNCTIONS


def convert():
    ct1 = float(tc_entry.get())
    ct2 = float(ct1 * 1.8)
    ct3 = float(ct2 + 32)
    tf_string.set("{:.1f}".format(ct3))

    # Celsius to Fahrenheit Formula: (°C * 1.8) + 32 = °F

    # Fahrenheit to Celsius Formula: (°F - 32) / 1.8 = °C


def clr():
    tc_string.set("")
    tf_string.set("")


def destroy():
    root.destroy()


c2f = Button(root, text="Convert ºC to ºF", command=convert, font=("Times", 18, "bold"))
c2f.place(x=75, y=200, width=150, height=30)

clr = Button(root, text="Clear", command=clr, font=("Times", 18, "bold"))
clr.place(x=275, y=200, width=150, height=30)

exit = Button(root, text="Exit", command=destroy, font=("Times", 18, "bold"))
exit.place(x=475, y=200, width=150, height=30)

root.mainloop()


# the main conversion
# window configuration
# user instruction and input
# shows result for opposite temp
# allow button to be clicked to convert
# add function for the button to convert from C to F
# bonus points for code to catch user input error
