#!/usr/bin/ env python 3
# Midterm project - Shopping List Array - Parallel Array

# shopping list and price list
s_list = [
    "Kvass",
    "Bread",
    "Borscht",
    "Butterbrod",
    "Pirozhki",
    "Pelmeni",
    "Blini",
    "Shashyk",
]
p_list = [2.50, 3.49, 9.95, 5.99, 3.99, 1.99, 3.00, 7.99]
print ("s_list p_list")

for i in range (len(items)):
    print(items[i]), " ", '$', price[i])
    
    
for index, i in enumerate(items):
    print (index,i)
    
    print ("Select item(s) from shopping list.")
    for i in range(1):
        index = int(input("Enter your item number: "))
        print(items[index], "$",price[index])
        
    for items in price:
        subtotal = price[index]
        print("sub total")
        print("$"+str(float(price[index])))
# Create and print a Parallel Array that matches each item to its price from both lists.
# should look like this... 1. Milk $2.99
# Print the array list with its index numbers.


# Select one or more items from the shopping list using the index number.
# Print your selected items with price


# Print sub total (base price of items before tax)
# Print sales tax amount (before adding it into total price)
# Calculate and print total price with tax included.
# Round to two decimal points


# Create three global variables with the proper data types
# sub_total
# total_price

# Sales tax is 8.9% - 0.089 - 8.9/100
def s_tax():
    global tax1
    tax1 = 8.9 / 100
    return tax1
