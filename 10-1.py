# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 01:53:22 2022

@author: CJA
"""
import numpy as np

#data = open("sample.txt")
data = open("input.txt")

sequence = [line for line in data.readlines()]
clockvals = [19, 59, 99, 139, 179, 219]
x = 1

clock = [[i, 0] for i in range(1, 241)]

index = 0

for tayne in sequence:
    if tayne[0] == "a":
        val = int(tayne[tayne.index(" "):])
        clock[index][1] = x
        index += 1
        clock[index][1] = x
        index += 1
        x += val
        clock[index][1] = x
    else:
        clock[index][1] = x
        index += 1

cumsum = 0

for val in clockvals:
    cumsum += np.prod(clock[val])

print(cumsum)