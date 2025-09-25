# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 14:16:28 2025

@author: qpy23cmu
"""

def square(i):
    return i**2

squares = []
i = 1
for i in range (100):
    squares.append(square(i))
    i += 1
    
print(squares)

x = 1
for x in range(squares):
    