#!/usr/bin/env python3
number1 = int(input("Enter the first number:\n"))
number2 = int(input("Enter the second number:\n"))
mult = number1 * number2
print(number1, "*" ,number2, "=", mult)
if mult > 0:
    print("The result is positive\n")
elif mult < 0:
    print("The result is negative\n")
else:
    print("The result is both positive and negative")
