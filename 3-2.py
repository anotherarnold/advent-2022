# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:17:09 2022

@author: CJA
"""

from aocd import get_data

file = get_data(day=3, year=2022)

def stringchecker(s1, s2, s3):
    for x in s2:
        for y in s1:
            for z in s3:
                if x == y == z:
                    return x

def priority(c):
    if ord(c) > 90:
        return(ord(c) - 96)
    else:
        return(ord(c) - 38)
    
cumsum = 0
comp = []
sack = []

for line in file.splitlines():
    sack.append(line)
    if len(sack)%3 == 0:
        comp.append(sack)
        sack = []

for bag in comp:
    ch = stringchecker(bag[0], bag[1], bag[2])
    cumsum += priority(ch)
    
print(cumsum)

