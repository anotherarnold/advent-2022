# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 04:51:17 2022

@author: CJA
"""

from aocd import get_data

file = get_data(day=6, year=2022)

#file = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

for i in range(len(file)):
    if len(set(file[i:i+4])) == 4:
        print(i+4)
        break