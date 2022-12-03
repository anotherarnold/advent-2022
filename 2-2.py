# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:52:05 2022

@author: CJA
"""
from aocd import get_data

file = get_data(day=2, year=2022)

#I wanted a nice clever solution using functions and objects, like we all love,
#but lists and dictionaries seem so much simpler
outcomes = [{"A X" : 3}, {"A Y" : 4}, {"A Z" : 8}, 
            {"B X" : 1}, {"B Y" : 5}, {'B Z' : 9}, 
            {"C X" : 2}, {"C Y" : 6}, {"C Z" : 7}]

cumscore = 0

for line in file.splitlines():
    for d in outcomes:
        if line in d.keys():
            cumscore += d[line]
            
print(cumscore)