# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 23:08:01 2025

@author: harry
"""

class State:
    
    def __init__(self, grid, pos= None):
        
        """
        grid: list of lists (n x n)
        pos: (i,j) position of emplty tile (0). 
        i = row
        j = column
        """
        self.size = len(grid)
        
        #copy grid
        self.grid = grid
        
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
    
    def clone(self):
        cPos = self.pos
        cGrid = [[self.grid[i][j] for j in range(self.size)] for i in range(self.size)]
        return State(cGrid,cPos)
        
    def moveUp(self):
        i,j = self.pos
        if i > 0: #check empty not in top row
            st = self.clone() #clone state
            st.grid[i][j],st.grid[i-1][j] = st.grid[i-1][j],st.grid[i][j] #swap empty with above tile
            st.pos = (i-1,j) #update position
            return st
        return None #move not possible
    
    def moveDown(self):
        i,j = self.pos
        if i+1 < self.size:
            st = self.clone()
            st.grid[i][j],st.grid[i+1][j] = st.grid[i+1][j],st.grid[i][j]
            st.pos = (i+1,j)
            return st
        return None
    
    def moveLeft(self):
        i,j = self.pos
        if j > 0:
            st = self.clone()
            st.grid[i][j],st.grid[i][j-1] = st.grid[i][j-1],st.grid[i][j]
            st.pos = (i,j-1)
            return st
        return None
    
    def moveRight(self):
        i,j = self.pos
        if j+1 < self.size:
            st = self.clone()
            st.grid[i][j],st.grid[i][j+1] = st.grid[i][j+1],st.grid[i][j]
            st.pos = (i,j+1)
            return st
        return None
    
    def move(self):
        actions = [self.moveDown,self.moveUp,self.moveRight,self.moveLeft]
        for fn in actions:
            result = fn()
            if result is not None:
                yield result
                print(" ")
                

    
def tester():
    grid = [[1,2,3],[4,0,5],[6,7,8]]
    st = State(grid)
    
    
    for next_state in st.move():
        print(next_state)
        
    print("second test")
    
    grid2 = [[1,2,3],[4,5,0],[6,7,8]]
    sa = State(grid2)
   
    for next_state in sa.move():
        print(next_state)
    


if __name__ == "__main__":
    tester()
    
