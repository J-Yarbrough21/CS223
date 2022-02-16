#!/usr/bin/env python3
import yaml
import string
import os
import re

sub_total = 0
total_price = 0
shopping_cart = {"bread": 1, "flour": 3, "vodka": 1}
sales_tax = 0
sales_tax_rate = 8.9
data = """
stock_list:
  - bread
  - eggs (doz)
  - kvass
  - catpoop
  - vodka
  - potatos
  - borscht
  - flour
  - bay leaf
  - teleportation juice
  - tasty fish
price_list:
  - 4.99
  - 2.99
  - 1.99
  - 6.99
  - 15.99
  - 5.99
  - 6.99
  - 3.99
  - 1.00
  - 15.99
  - 9.99
"""


def load_yaml_to_dict():
    load_data = yaml.load(data, Loader=yaml.CLoader)
    print(load_data)
    if len(load_data["stock_list"]) != len(load_data["price_list"]):
        raise ValueError("ERROR: Stock database is corrupted!")
    stock = dict(zip(load_data["stock_list"], load_data["price_list"]))
    print(stock)
    sorted_keys = sorted(stock)
    print(sorted_keys)
    return stock


def print_price_table(stock):
    lines = []
    sorted_keys = sorted(stock)
    for index, key in enumerate(sorted_keys):
        item = "{}"
        fmt_index = "{:>4}".format("{}. ".format(index + 1))
        fmt_price = "{:>8}".format("${:.2f}".format(stock[key]))
        lines.append("{:<}{:26}{} |".format(fmt_index, key, fmt_price))
    return lines


def print_cart_table(cart, stock):
    lines = []
    for item in cart.keys():
        sub_total = stock[item] * cart[item]
        fmt_price = "{:>8}".format("${:.2f}".format(sub_total))
        lines.append("| {:23}{:<5} {}".format(item, cart[item], fmt_price))
    return lines


def total_cart(cart, stock):
    sub_total = 0.0
    for item in cart.keys():
        sub_total += stock[item] * cart[item]
    return sub_total


def tax_amt(sub_total):
    global sales_tax_rate
    return sub_total * (sales_tax_rate / 100)


def print_stock_and_cart(price_table, cart_table):
    count = max([len(price_table), len(cart_table)])
    # print(price_table)-
    for index in range(0, count + 1):
        try:
            if index >= len(price_table):
                x = ""
            else:
                x = price_table[index]
            if index >= len(cart_table):
                y = ""
            else:
                y = cart_table[index]
        except:
            print("borked!")
        if x or y:
            print("{:<38}{:<}".format(x, y))
    return


def print_cart_totals(cart, stock):
    cart_total = total_cart(cart, stock)
    taxes = tax_amt(cart_total)
    grand_total = cart_total + taxes
    fmt_cart_total = "{:>20}".format("${:.2f}".format(cart_total))
    fmt_taxes = "{:>23}".format("${:.2f}".format(taxes))
    fmt_grand = "{:>25}".format("${:.2f}".format(grand_total))
    print(" " * 39 + "|| SubTotal of Items:{}".format(fmt_cart_total))
    print(" " * 39 + "|| Sales Tax Due: {}".format(fmt_taxes))
    print(" " * 39 + "|| Grand Total: {}".format(fmt_grand))
    return


def is_non_supported_alpha(input, reserved=[]):
    """
    return true if input is not a reserved character.
    return false otherwise
    """
    retval = False
    non_sup_char = "".join(
        [x for x in list(string.ascii_lowercase) if x not in reserved]
    )
    non_sup_char += string.ascii_uppercase + string.punctuation
    non_list = list(non_sup_char)
    if [x for x in list(input) if x in non_list]:
        retval = True
    return retval


def is_float(input):
    retval = False
    if re.match(r"\d*\.\d*", input):
        retval = True
    return retval


def is_not_int_str(input):
    print(input)
    retval = True
    if re.search(r"^[\d]+$", input):
        retval = False
    return retval


def is_valid_index(input, stock):
    return input in range(1, len(sorted(stock)) + 1)


def valid_item_input(input):
    ret_val = True
    if is_float(input):
        # print("2")
        ret_val = False
    if is_not_int_str(input):
        # print("3")
        ret_val = False
    # print(ret_val)
    return ret_val


def validate_quant_input(input):
    ret_val = True
    if is_non_supported_alpha(input):
        ret_val = False
    if is_float(input):
        ret_val = False
    if is_not_int_str(input):
        ret_val = False
    if input == "":
        ret_val = True
    return ret_val


def add_item_to_cart(item, amt, cart):
    if item in cart.keys():
        cart[item] += amt
    else:
        cart[item] = amt
    return cart


def save_cart(cart, stock):
    raw_file = input("Please enter path and filename: ")
    try:
        with open(raw_file, "w") as target:
            for line in print_cart_table(cart, stock):
                target.write(line)
    except Exception:
        print("Failed to open and write the shopping cart to the file.")
    return


def get_user_input(stock, cart):
    print(
        'To exit, enter "x" for the item. To save the cart to a file and exit, enter'
        + '"s" for the item.'
    )
    item = None
    while not item:
        print("Please enter the item number and quantity you wish to add to your cart")
        raw_item = input("Please enter item number: ")
        if not is_non_supported_alpha(raw_item, ["x", "s"]):
            if raw_item in ["x", "s"]:
                if raw_item == "s":
                    save_cart(cart, stock)
                exit()
        if valid_item_input(raw_item):
            try:
                tmp_item = int(raw_item)
            except TypeError:
                print("Please enter a item value in the range of the shown ID.")
            if is_valid_index(tmp_item, stock):
                item = sorted(stock)[tmp_item - 1]
    raw_item = None
    print("You selected: {}".format(item))
    quantity = None
    while not quantity:
        raw_quantity = input(
            "Please enter the quantity of the item you want (default is 1): "
        )
        if validate_quant_input(raw_quantity):
            if not raw_quantity:
                raw_quantity = "1"
            try:
                quantity = int(raw_quantity)
            except TypeError:
                print("Please enter a item value in the range of the shown ID.")
    raw_quantity = None
    cart = add_item_to_cart(item, quantity, cart)
    return cart


def main():
    stock = load_yaml_to_dict()
    shopping_cart = {}
    input("Press Enter to Continue.")
    print("")
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        stock_headers = "{:<3}{:<30}{:<}".format("ID", "Item Name", "Price")
        cart_headers = "{:<23}{:<6}{:<8}".format("Item Name", "Count", "Subtotal")
        print("{:<38} || {:<}".format("Stock", "Cart"))
        print("{:<38} || {:<}".format(stock_headers, cart_headers))
        price_table = print_price_table(stock)
        cart_table = print_cart_table(shopping_cart, stock)
        print_stock_and_cart(price_table, cart_table)
        print_cart_totals(shopping_cart, stock)
        shopping_cart = get_user_input(stock, shopping_cart)
    return


if __name__ == "__main__":
    main()
