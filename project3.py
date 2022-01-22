#!/usr/bin/env python3

from tkinter import *
from turtle import clear

root = Tk()
root.geometry("600x300")
root.title("Future Value Calculator from the Bank of Jennifer")

# USER INPUT LABELS AND BOXES
label = Label(
    root,
    text="Monthly Investment: ",
    font=("Times", 18, "bold"),
    fg="#00FFFF",
    justify=("right"),
)

mi_string = StringVar()
label.place(x=0, y=20, width=200, height=30)
mi_entry = Entry(root, textvariable=mi_string, font=("Times", 18))
mi_entry.place(x=225, y=20, width=200, height=30)


label = Label(
    root,
    text="Years Saved: ",
    font=("Times", 18, "bold"),
    fg="#00FFFF",
    justify=("right"),
)
yl_string = StringVar()
label.place(x=0, y=60, width=200, height=30)
yl_entry = Entry(root, textvariable=yl_string, font=("Times", 18))
yl_entry.place(x=225, y=60, width=200, height=30)


# OUTPUT

label = Label(
    root,
    text="Total Years Future Value: ",
    font=("Times", 18, "bold"),
    fg="#00FFFF",
    justify=("right"),
)
yfv_string = StringVar()
label.place(x=0, y=100, width=200, height=30)
yfv_entry = Entry(root, textvariable=yfv_string, font=("Times", 18))
yfv_entry.place(x=225, y=100, width=200, height=30)

# FUNCTIONS


def m_int(apy=9.50):  # takes yearly interest rate and converts to monthly rate
    return (apy / 100) / 12


def num_months():  # converts users Years Saved input into months
    years = float(yl_entry.get())
    return int(years * 12)


def calculate():
    total = 0
    monthly_invest = float(mi_entry.get())
    for month in range(1, num_months() + 1):
        sub_total = total + monthly_invest
        interest = sub_total * m_int()
        total = sub_total + interest
        print(month, sub_total, total)
    yfv_string.set("{:.2f}".format(total))


def clear():
    mi_string.set.format("")
    yl_string.set("")
    yfv_string.set("")


def destroy():
    root.destroy()


# BUTTONS

calc1 = Button(root, text="Calculate", command=calculate, font=("Times", 12, "bold"))
calc1.place(x=25, y=200, width=150, height=30)

clear = Button(root, text="Clear", command=calculate, font=("Times", 12, "bold"))
clear.place(x=225, y=200, width=150, height=30)

exit = Button(root, text="Exit", command=destroy, font=("Times", 12, "bold"))
exit.place(x=425, y=200, width=150, height=30)

root.mainloop()
