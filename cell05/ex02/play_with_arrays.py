#!/usr/bin/env python3
arrayori = [2, 8, 9, 48, 8, 22, -12, 2]
print(arrayori)
arraynew = []
for i in range(len(arrayori)):
    if arrayori[i] > 5:
        arraynew.append(arrayori[i] + 2)
print(arraynew)