# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 15:03:09 2022

@author: CJA
"""

from aocd import get_data

file = get_data(day=4, year=2022)

#file = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"

def chunker(s):
    l = []
    for line in s.splitlines():
        l.append(line.split(","))
    return l

elfjobs = chunker(file)
cumsum = 0

for job in elfjobs:
    x = job[0].split("-")
    y = job[1].split("-")
    q = range(int(x[0]), int(x[1])+1)
    v = range(int(y[0]), int(y[1])+1)
    if set(q).issuperset(set(v)) or set(v).issuperset(set(q)):
        cumsum += 1

print(cumsum)