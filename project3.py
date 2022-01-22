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
label.place(x=0, y=20, width=200, height=30)

mi_entry = Entry(root, font=("Times", 18))
mi_entry.place(x=225, y=20, width=200, height=30)

label = Label(
    root,
    text="Years Saved: ",
    font=("Times", 18, "bold"),
    fg="#00FFFF",
    justify=("right"),
)
label.place(x=0, y=60, width=200, height=30)

yl_entry = Entry(root, font=("Times", 18))
yl_entry.place(x=225, y=60, width=200, height=30)

# FUNCTIONS
# the 'self' keyword is only used if you are defining a function that is a
# member of a class.  No class, no self.
# when using the function in arithmitic or other operations, it MUST return a
# result of the type needed for the operation.
def m_int(apy=9.50):
    return (apy / 100) / 12


def months1():
    years = float(mi_entry.get())
    months = years * 12
    months1 = months


def fut_val1():
    mi_1 = float(mi_entry.get())
    fv_1a = float(mi_1) * (1 + m_int)
    fut_val1 = fv_1a


def fut_val2():
    mi_1 = float(mi_entry.get())
    fv_1a = float(mi_1) * (1 + m_int)
    fut_val2 = fv_1a


def calculate():
    user_pv = mi_entry.get()
    future_value1 = (user_pv)(1 + m_int)
    future_value2 = (user_pv)(1 + m_int)
    FV3 = future_value1 * future_value2
    total_future_value = FV3


def clear():
    mi_entry.delete(0, END)
    yl_entry.delete(0, END)
    yfv_entry.delete(0, END)


def destroy():
    root.destroy()


# OUTPUTS
label = Label(
    root,
    text="Future Value: ",
    font=("Times", 18, "bold"),
    fg="#00FFFF",
    justify=("right"),
)
label.place(x=0, y=100, width=200, height=30)
yfv_entry = Entry(root, textvariable="", font=("Times", 12))
yfv_entry.place(x=225, y=100, width=200, height=30)

# BUTTONS

calc1 = Button(root, text="Calculate", command=calculate, font=("Times", 12, "bold"))
calc1.place(x=25, y=200, width=150, height=30)

clear = Button(root, text="Clear", command=calculate, font=("Times", 12, "bold"))
clear.place(x=225, y=200, width=150, height=30)

exit = Button(root, text="Exit", command=destroy, font=("Times", 12, "bold"))
exit.place(x=425, y=200, width=150, height=30)

root.mainloop()


# future Value formula FV=PV(1+i)to the "n" power
# FV1= (PV=mi_entry)(1+ i = interest2)
# FV2 = FV1 * FV1

# mi_1 = mi_entry.get

# Years = yl_entry.get
# Months = years * 12
# fv_2 = Months

# interest1 = 9.50/100 = annual rate converted to decimal
# interest2 = interest1/12 = monthly interest rate
# m_int = interest2

# simple interest = PxRxT P=Principal R=Rate T=Time
# future Value formula FV=PV(1+i)to the "n" power
# FV = Future value (float)
# PV = present value (float)
# i = interest rate per period in decimal form interest rate = 0.095
# n = the number of time periods

# Button(window,text="Change Text",command=change_text).grid(row=count, column=0)
# button1 calculate
# button two exit


# create the necessary buttons - y/n continue
# properly define the functions
# convert yearly values to monthly values
# calculate future value
# call the functions
