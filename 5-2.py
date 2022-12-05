# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 00:22:01 2022

@author: CJA
"""
data = open("input.txt")

#data = open("sample.txt")

file = ""

for line in data.readlines():    
    file += line

data.close()

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
            s = line.replace("move ", "")
            s = s.replace("from ", "")
            s = s.replace("to ", "")
            c = s.split(" ")  
            d= []
            for n in c:
                d.append(int(n))
            commands.append(d)
    return commands

def boattracker(h):
    boats = []
    i = 0
    while i < h.index("\n"):
        if i % 4 == 0:
            boats.append([])
        i += 1
    for line in h.splitlines():
        i = 0
        k = 0
        while i < len(line):
            if i % 4 == 0:
                if line[i].isalpha():
                    boats[k].append(line[i])
                k += 1
            i += 1
    return boats

def movers(boat, mov):
    for move in mov:
        i = 0
        while i < move[0]:
            x = boat[move[1]-1].pop(0)
            boat[move[2]-1].insert(i, x)
            i += 1
            

boats = boattracker(headerget(file))

moves = commandgrab(file)

movers(boats, moves)

answer = ""
for boat in boats:
    answer += boat[0]

print(answer)


    