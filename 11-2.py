# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 02:15:43 2022

@author: CJA
"""
import numpy as np

#file = open("sample.txt")
file = open("input.txt")

data = file.readlines()

file.close()
mod = 1
class Monkey():
    def __init__(self):
        self.items = []
        self.operation = ""
        self.divisor = 1
        self.monkey_true = 0
        self.monkey_false = 0
        self.inspections = 0
    
    def monkey_test(self, x):
        if x % self.divisor == 0:
            return self.monkey_true
        else:
            return self.monkey_false
    
def operate(operation, x):
    if operation[0] == "*":
        if operation[operation.index(" ")+1].isnumeric():
            return int((x * int(operation[operation.index(" "):])) % mod)
        else:
            return int((x * x) % mod)
    else:
        if operation[operation.index(" ")+1].isnumeric():
            return int((x + int(operation[operation.index(" "):])) % mod)
        else:
            return int((x + x) % mod)
 
monkeys = [Monkey() for i, line in enumerate(data) if i % 7 == 0]

for index, line in enumerate(data):
    i = int(index / 7)
    if index % 7 == 1:
        start = line[line.index(": ")+1:].split(",")
        for item in start:
            monkeys[i].items.append(int(item))
    if index % 7 == 2:        
        monkeys[i].operation = line[line.index("d")+2:-1]
    if index % 7 == 3:
        monkeys[i].divisor = int(line[line.index("y")+1:])
    if index % 7 == 4:
        monkeys[i].monkey_true = int(line[line.index("y")+1:])
    if index % 7 == 5:
        monkeys[i].monkey_false = int(line[line.index("y")+1:])

#I got a hint for this, i was about 70% the way there but would never have thought
#to take the product with my tiny sub-brain
mod = np.prod([m.divisor for m in monkeys])

for i in range(10000):
    for m in monkeys:
        while len(m.items) > 0:
            x = m.items.pop()
            m.inspections += 1
            y = operate(m.operation, x)
            monkeys[m.monkey_test(y)].items.append(y)
          
counts = [monkey.inspections for monkey in monkeys]
highest = counts.pop(counts.index(max(counts)))
print(highest * max(counts))