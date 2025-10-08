# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 12:41:05 2025

@author: harry
"""

import time 
import timeit

def compute_for_a_while():
    for i in range(1000000):
        pass
    
"""
start_time = time.perf_counter()
compute_for_a_while()
end_time = time.perf_counter()
print("Time:", end_time-start_time,"seconds")
"""
def test():
    """simple test function"""
    l = [i for i in range(100)]

if __name__ == '__main__':
    print(timeit.timeit("test()",
          setup="from __main__ import test",number=10))