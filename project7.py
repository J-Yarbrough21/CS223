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
print("s_list p_list")

for i in range(len(s_list)):
    print(s_list[i]), " ", "$", (p_list[i])

for index, i in enumerate(s_list):
    print(index, i)
    print("Select item(s) from shopping list.")

for i in range(1):
    index = int(input("Enter your item number: "))
    print(s_list[index], "$", p_list[index])

for items in p_list:
    subtotal = p_list[index]
    print("sub total")
    print("$" + str(float(p_list[index])))


def s_tax():
    global tax1
    tax1 = 8.9 / 100
    return tax1


def sub_total():
    global sb_1
    sb_1 = subtotal
    return sb_1


print("$", round(sub_total(), 2))


def sub_tax_total():
    global stt
    stt = sub_total * s_tax
    return stt


print("$", round(sub_tax_total(), 2))
