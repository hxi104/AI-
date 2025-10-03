# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 23:08:01 2025

@author: harry
"""

class State:
    
    def __init__(self, grid, pos = None):
        
        """
        grid: list of lists (n x n)
        pos: (i,j) position of emplty tile (0). 
        i = row
        j = column
        """
        self.size = len(grid)
        
        #copy grid
        self.grid = [[grid[i][j] for j in range(self.size)] for i in range(self.size)]
        
        if pos is None:
            for i in range(self.size):
                for j in range(self.size):
                    if self.grid[i][j] == 0:
                        self.pos = (i,j)
                        break
        else:
            self.pos = pos
            
    def __str__(self):
        """
        return a readable string representation of the grid
        """
        rows = []
        for row in self.grid:
            rows.append(' '.join(f"{v:2d}" if v !=0 else " _" for v in row))
        return '\n'.join(rows)
        
        
    
def tester():
    grid = [[1,0,3],[4,2,5],[6,7,8]]
    st = State(grid)
    print("empty tile position:", st.pos)
    
    print(st)


if __name__ == "__main__":
    tester()
    
