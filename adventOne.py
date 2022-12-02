# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:56:42 2022

@author: CJA
"""

foo = open('input.txt')

fooTwo = foo.readlines()

foo.close()

for i in range(len(fooTwo)):
    fooTwo[i] = fooTwo[i][:-1]
    if fooTwo[i] == "":
        fooTwo[i] = -69
    else:
        fooTwo[i] = int(fooTwo[i])

tracksum = 0
best = 0

for f in fooTwo:
    if f != -69:
        tracksum = tracksum + f
    else:
        if tracksum > best:
            best = tracksum
            tracksum = 0
        else:
            tracksum = 0
            
print(best)