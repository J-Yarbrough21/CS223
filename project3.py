#!/usr/bin/env python3
from tkinter import *

window = Tk()
window.geometry("900x900")
window.title("The Bank of Jennifer - Future Value Calculator")


def main():
    print("Welcome to The Bank of Jennifer - Future Value Calculator\n")


# interest_rate = 0.95
choice = "Y"
while choice.lower() == "y":

    def calculate_future_value(monthly_investment, yearly_interest, years):
        # convert yearly values to monthly values
        monthly_interest_rate = yearly_interest / 12 / 100
        month = years * 12

        future_value = 0.0
        for i in range(0, month):
            future_value += monthly_investment
            monthly_interest = future_value * monthly_interest_rate
            future_value += monthly_interest
        return future_value


def main():
    choice = "Y"
    while choice.lower() == "y":

        # Get input from user
        monthly_investment = float(input("Enter Monthly Investment Amount: \t"))
        yearly_interest_rate = float(input("Enter Yearly Interest Rate: \t"))
        years = int(input("Enter Number of Years : \t\t"))


# Get future_value
future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years)

# display the result
print("Future value:\t\t\t" + str(round(future_value, 2)))
print()

# see if the user wants to continue using the program
choice = input("Continue (y/n)?: ")
print()

print("Bye")

if main == "_main":
    main()

# create the GUI
# make the title your fake bank name ie JY Bank Future Value Calculator
# hard code the interest rate to 9.5%
# create the necessary buttons - y/n continue
# properly define the functions
# convert yearly values to monthly values
# calculate future value
# call the functions
# view like Exercise 3-3

window.mainloop()
