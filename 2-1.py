# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:52:05 2022

@author: CJA
"""
from aocd import get_data

file = get_data(day=2, year=2022)

#Since there are only 9 outcomes it seemed simpler to use dicts
outcomes = [{"A X" : 4}, {"A Y" : 8}, {"A Z" : 3}, 
            {"B X" : 1}, {"B Y" : 5}, {'B Z' : 9}, 
            {"C X" : 7}, {"C Y" : 2}, {"C Z" : 6}]

cumscore = 0

for line in file.splitlines():
    for d in outcomes:
        if line in d.keys():
            cumscore += d[line]
            
print(cumscore)