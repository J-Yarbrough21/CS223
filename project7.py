#!/usr/bin/env python 3
# Midterm project - Shopping List Array - Parallel Array

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
p_list = [2.50, 3.49, 9.95, 5.99, 3.99, 1.99, 3.99, 7.99]

shopping_cart = []
subtotal = 0


def sub_tax_total():
    global stt
    stt = subtotal * s_tax()
    return stt


def s_tax():
    global tax1
    tax1 = 8.9 / 100
    return tax1


def main(sub_tax_total, s_tax):
    global subtotal

    print("Select item(s) from shopping list.")
    for index, i in enumerate(s_list):
        print("{}. {:<32} {:.2f}".format(index + 1, i, p_list[index]))

    for i in range(1):
        index = int(input("Enter your item number: "))
        print(s_list[index], "$", p_list[index])
        shopping_cart.append(index)
        print("Your current cart is: ")

        for item in shopping_cart:
            print(s_list[item])
            subtotal += p_list[item]
            print("Sub Total: ${:.2f}".format(round(subtotal, 2)))
            print("Sales Tax: ${:.2f}".format(round(sub_tax_total(), 2)))
            print("Total: ${:.2f}".format(round(subtotal + sub_tax_total(), 2)))


if __name__ == "__main__":
    main(sub_tax_total, s_tax)
