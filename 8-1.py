# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:32:41 2022

@author: CJA
"""
from aocd import get_data
import numpy as np

data = get_data(day=8, year=2022)

forest = np.array([[int(char) for char in line if char.isnumeric()] for line in data.splitlines()])

y, x = np.shape(forest)
treey, treex = y -1, x - 1
visibletrees = set()

for iy, row in enumerate(forest):
    for ix, cell in enumerate(row):        
        if iy > 0 and iy < treey and ix > 0 and ix < treex:
            edges = [forest[iy][:ix], forest[iy][ix+1:], 
                     np.transpose(forest)[ix][:iy], np.transpose(forest)[ix][iy+1:]]
            for group in edges:
                if np.all(group < cell):
                    visibletrees.add((ix, iy, cell))
                    
print(len(visibletrees) + (y+x) * 2 - 4)