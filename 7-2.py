# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:23:55 2022

@author: CJA
"""
#I had to get hints for this one
#I had three different solutions, one brute forced, one recursive, and one using 
#a tree, that all worked on the sample input but not the full input.
#so I had to figure out this simpler strategy

#data = open("sampleTwo.txt").read()
#data = open("sample.txt").read()
data = open("input.txt").read()

path = []
#I don't use dicts enough!
tree = {}

for line in data.splitlines():
    if line == "$ cd ..":
        path.pop()
        #I had forgotten continue was a keyword in python lol
        continue
    
    if line[:4] == "$ cd":
        path.append(line[5:])
        
        if "".join(path) not in tree.keys():
            tree.update({ "".join(path): 0 })
        
        continue
    
    if line[0].isnumeric():
        size = int(line[:line.index(" ")])
        pwd = []
        
        for d in path:
            pwd.append(d)
            tree.update({ ''.join(pwd): tree[''.join(pwd)] + size})
            #print(tree)
            
        continue

for val in sorted(list(tree.values())):
    if val > 30000000 - (70000000 - tree['/']):
        print(val)