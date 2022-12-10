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

linecounts = [[i for i in range(0, 40)], [i for i in range(40, 80)], 
              [i for i in range(80, 120)], [i for i in range(120, 160)], 
              [i for i in range(160, 200)], [i for i in range(200, 240)]]

for index, count in enumerate(linecounts):
    for i in count:
        if i - min(count) in range(clock[i] - 1, clock[i] + 2):
            lines[index] += "#"
        else:
            lines[index] += "."

for line in lines:
    print(line)
