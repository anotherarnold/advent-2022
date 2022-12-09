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
        if iy > 0 and iy < treey and ix > 0 and ix < (treex):
            #edge 0 = left, edge 1 = right, edge 2 = above, edge 3 = below
            edges = [np.flip(forest[iy][:ix]), forest[iy][ix+1:], 
                     np.flip(np.transpose(forest)[ix][:iy]), np.transpose(forest)[ix][iy+1:]]
            viewscore = [0, 0, 0, 0]
            for i, group in enumerate(edges):
                for z, coord in enumerate(group):
                    if coord < cell:
                        viewscore[i] = z + 1
                    elif coord >= cell:
                        viewscore[i] = z + 1
                        break
                    else:
                        break
            visibletrees.add(np.prod(viewscore))

print("Max: ", max(visibletrees))
