# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 14:16:28 2025

@author: qpy23cmu
"""

def square(i):
    return i**2

squares_list = [square(i) for i in range(1,101)]
#for value in squares_list:
    #print(value)
print("example 2")
def next_square():
    i = 1
    while True:
        yield i ** 2
        i += 1 
        
gen = next_square()

for _ in range(100):
    print(next(gen))
    
    #optional
    import sys
print("list memory usage:",sys.getsizeof(squares_list),"bytes")
print("generator memory usage:",sys.getsizeof(next_square()),"bytes")
    