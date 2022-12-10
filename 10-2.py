# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 01:53:22 2022

@author: CJA
"""
#data = open("sample.txt")
data = open("input.txt")

sequence = [line for line in data.readlines()]
x = 1
clock = [0 for i in range(1, 241)]
index = 0

for tayne in sequence:
    if tayne[0] == "a":
        val = int(tayne[tayne.index(" "):])
        clock[index] = x
        index += 1
        clock[index] = x
        index += 1
        x += val
        clock[index] = x
    else:
        clock[index] = x
        index += 1

lines= ["", "", "", "", "", ""]

for i in range(240):
    if i < 40:
        if i in range(clock[i] - 1, clock[i] + 2):
            lines[0] += "#"
        else:
            lines[0] += "."
    elif i < 80:
        if i - 40 in range(clock[i] - 1, clock[i] + 2):
            lines[1] += "#"
        else:
            lines[1] += "."
    elif i < 120:
        if i - 80 in range(clock[i] - 1, clock[i] + 2):
            lines[2] += "#"
        else:
            lines[2] += "."
    elif i < 160:
        if i - 120 in range(clock[i] - 1, clock[i] + 2):
            lines[3] += "#"
        else:
            lines[3] += "."
    elif i < 200:
        if i - 160 in range(clock[i] - 1, clock[i] + 2):
            lines[4] += "#"
        else:
            lines[4] += "."
    else:
        if i - 200 in range(clock[i] - 1, clock[i] + 2):
            lines[5] += "#"
        else:
            lines[5] += "."
            
for line in lines:
    print(line)
