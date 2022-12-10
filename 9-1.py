# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 21:46:07 2022

@author: CJA
"""
import numpy as np

data = open("input.txt")
#data = open("sample.txt")

def moveparse(x):
    move = x.split(" ")
    move[1] = int(move[1])
    return move

moves = list(map(moveparse, [line for line in data.readlines()]))

head_pos = [0, 0]
tail_pos = [0, 0]
movement = {"R" : [1, 0], "L": [-1, 0], "U" : [0, 1], "D": [0, -1]}
count = set()

for move in moves:
    i = 0
    while i < move[1]:
        head_pos = list(np.array(head_pos) + np.array(movement[move[0]]))
        diff = list(np.array(head_pos) - np.array(tail_pos))
        if abs(diff[0]) > 1:
            if diff[0] > 0:
                tail_pos[0] += 1
            else:
                tail_pos[0] += -1
            #This probably shouldn't work but did, it doesn't for pt 2
            if abs(diff[1]) > 0:
                tail_pos[1] += diff[1]
        if abs(diff[1]) > 1:
            if diff[1] > 0:
                tail_pos[1] += 1
            else:
                tail_pos[1] += -1
            if abs(diff[0]) > 0:
                tail_pos[0] += diff[0]
        count.add((tail_pos[0], tail_pos[1]))
        i += 1    

print(len(count))