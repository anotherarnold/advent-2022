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
bestOne = 0
bestTwo = 0
bestThree = 0

for f in fooTwo:
    if f != -69:
        tracksum = tracksum + f
    else:
        if tracksum > bestOne:
            bestOne = tracksum
            tracksum = 0
        elif tracksum > bestTwo:
            bestTwo = tracksum
            tracksum = 0
        elif tracksum > bestThree:
            bestThree = tracksum
            tracksum = 0
        else:
            tracksum = 0
            
print("1st: ", bestOne)
print("\n2nd: ", bestTwo)
print("\n3rd: ", bestThree)
print("\nSum: ", bestOne + bestTwo + bestThree)