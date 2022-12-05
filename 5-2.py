# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 00:22:01 2022
@author: CJA
"""
def headerget(f):
    header = ""
    for line in f.splitlines():
        if len(line) > 1:
            header += line[1:-1] + "\n"
        else:
            header = header[:-1]
            break
    return header

def commandgrab(f):
    commands= []
    for line in f.splitlines():
        if len(line) > 0 and line[0] == "m":
            s = line.replace("move ", "").replace("from ", "").replace("to ", "")
            c = list(map(lambda x: int(x), s.split(" ")))
            commands.append(c)
    return commands

def boattracker(h):
    boats = [[] for x in range(h.index("\n")) if x % 4 == 0]
    for line in h.splitlines():
        i = 0
        b = 0
        while i < len(line):
            if i % 4 == 0:
                if line[i].isalpha():
                    boats[b].append(line[i])
                b += 1
            i += 1
    return boats

def movers(boat, mov):
    for move in mov:
        i = 0
        while i < move[0]:
            x = boat[move[1]-1].pop(0)
            boat[move[2]-1].insert(i, x)
            i += 1          

data = open("input.txt")

file = "".join(line for line in data.readlines())

data.close()

boats = boattracker(headerget(file))

movers(boats, commandgrab(file))

print("".join(boat[0] for boat in boats))
