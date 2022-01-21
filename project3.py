#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.geometry("900x900")
root.title("Future Value Calculator from the Bank of Jennifer")

# User Input Labels and Entry Boxes
label = Label(
    root,
    text="Monthly Investment",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=5, y=20, width=150, height=30)

mi_entry = Entry(root, font=("Times", 12))
mi_entry.place(x=35, y=55, width=150, height=30)

label = Label(
    root, text="Years Saved", font=("Times", 12, "bold"), fg="#030303", justify=("left")
)
label.place(x=5, y=20, width=150, height=30)

yl_entry = Entry(root, font=("Times", 12))
yl_entry.place(x=35, y=55, width=150, height=30)

root.mainloop()

# create the GUI
# make the title your fake bank name ie JY Bank Future Value Calculator
# hard code the interest rate to 9.5%
# create the necessary buttons - y/n continue
# properly define the functions
# convert yearly values to monthly values
# calculate future value
# call the functions
# view like Exercise 3-3
