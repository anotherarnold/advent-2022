# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:48:14 2022

@author: CJA
"""

from aocd import get_data

file = get_data(day=3, year=2022)

def stringsplitter(s):
    return([s[slice(0, len(s)//2)], s[slice(len(s)//2, len(s))]])

def stringchecker(s1, s2):
    for x in s2:
        for y in s1:
            if x == y:
                return x

def priority(c):
    if ord(c) > 90:
        return(ord(c) - 96)
    else:
        return(ord(c) - 38)
    
cumsum = 0

for line in file.splitlines():
    l = stringsplitter(line)
    cumsum += priority(stringchecker(l[0], l[1]))

print(cumsum)