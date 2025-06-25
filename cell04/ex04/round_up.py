#!/usr/bin/env python3
import math
number_input = input("Give me a number: ")
try:
    number = float(number_input)
    print(math.ceil(number))
except ValueError:
    print("That's not a valid number.")