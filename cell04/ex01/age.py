#!/usr/bin/env python3
age = int(input("Please tell me your age: "))
print("You are currently", age, "years old")
i = 10
while i < 40:
    newage = age + i
    print("In", i, "years, you'll be", newage,"years old.")
    i += 10