#!/usr/bin/env python3

from tkinter import *
import tkinter as tk
import tkinter.font as tkFont


root = tk.Tk()
root.geometry("900x900")
root.title("The Bank of Jennifer - Future Value Calculator")
ft = tkFont.Font(family="Times", size=14, weight="bold")

mi_label = Label(
    root, text="Enter the Monthly Investment Amount.", font=("Times", 12, "bold")
)
mi_label.place(x=10, y=10)

yl_label = Label(
    root,
    text="Enter the Number of Years you would like to save ",
    font=("Times", 12, "bold"),
)
yl_label.place(x=50, y=10)


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
