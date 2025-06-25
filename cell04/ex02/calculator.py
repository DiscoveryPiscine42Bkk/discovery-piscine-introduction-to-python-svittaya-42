#!/usr/bin/env python3
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
print("Thank you!")

for op in "+-/*":
    print(number1, op, number2, "=", eval(f"{number1}{op}{number2}"))