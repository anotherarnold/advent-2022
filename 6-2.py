# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 05:20:37 2022

@author: CJA
"""

from aocd import get_data

file = get_data(day=6, year=2022)

#file = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

for i in range(len(file)):
    if len(set(file[i:i+14])) == 14:
        print(i+14)
        break