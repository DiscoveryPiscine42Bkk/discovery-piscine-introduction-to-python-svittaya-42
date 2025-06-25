#!/usr/bin/env python3
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

num_input = input("Give me a number: ")

if is_float(num_input):
    num = float(num_input)
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
else:
    print("That's not a valid number.")