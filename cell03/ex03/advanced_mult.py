#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 1
    while i <= 10:
        print(f"Table de {i}:", end=" ")
        j = 0
        result = 0
        while j <= 10:
            print(result, end=" ")
            result += i  # add i instead of doing i * j
            j += 1
        print()
        i += 1