#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.geometry("900x900")
root.title("Future Value Calculator from the Bank of Jennifer")

# User Input Labels and Entry Boxes
label = Label(
    root,
    text="Monthly Investment: ",
    font=("Times", 18, "bold"),
    fg="#00FFFF",
    justify=("right"),
)
label.place(x=0, y=10, width=200, height=30)

mi_entry = Entry(root, font=("Times", 18))
mi_entry.place(x=185, y=10, width=200, height=30)

label = Label(
    root,
    text="Years Saved: ",
    font=("Times", 18, "bold"),
    fg="#00FFFF",
    justify=("right"),
)
label.place(x=350, y=10, width=200, height=30)

yl_entry = Entry(root, font=("Times", 18))
yl_entry.place(x=500, y=10, width=200, height=30)


def m_int(self):
    int1 = 9.50 / 100
    int2 = int1 / 12
    m_int = int2


def months1(self):
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

    # future Value formula FV=PV(1+m_int)to the "n" power
    # FV1= (PV=mi_entry)(1+ i = interest2)
    # FV2 = FV1 * FV2

    # Out Put Boxes
    # Yearly Future Value

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

# hard code the interest rate to 9.5%
# create the necessary buttons - y/n continue
# properly define the functions
# convert yearly values to monthly values
# calculate future value
# call the functions
