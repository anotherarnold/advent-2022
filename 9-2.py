# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 21:46:07 2022

@author: CJA
"""
import numpy as np

data = open("input.txt")
#data = open("sample.txt")
#data = open("sample_two.txt")

def moveparse(x):
    move = x.split(" ")
    move[1] = int(move[1])
    return move

moves = list(map(moveparse, [line for line in data.readlines()]))

knots = [[0, 0] for i in range(10)]
movement = {"R" : [1, 0], "L": [-1, 0], "U" : [0, 1], "D": [0, -1]}
count = set()

for move in moves:
    i = 0
    while i < move[1]:
        knots[0] = list(np.array(knots[0]) + np.array(movement[move[0]]))
        for index in range(1, len(knots)):
            diff = list(np.array(knots[index - 1]) - np.array(knots[index]))
            if abs(diff[0]) > 1:
                if diff[0] > 0:
                    knots[index][0] += 1
                else:
                    knots[index][0] += -1
                if abs(diff[1]) == 1:
                    knots[index][1] += diff[1]
            if abs(diff[1]) > 1:
                if diff[1] > 0:
                    knots[index][1] += 1
                else:
                    knots[index][1] += -1
                if abs(diff[0]) == 1:
                    knots[index][0] += diff[0]
            count.add((knots[-1][0], knots[-1][1]))
        
        i += 1    

print(len(count))