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
        cPos = self.pos[0],self.pos[1]
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
        actions = [
        ("down", self.moveDown),
        ("up", self.moveUp),
        ("left", self.moveLeft),
        ("right", self.moveRight)
        ]
        for name,fn in actions:
            result = fn()
            if result is not None:
                yield name, result
                
                
    def tPos(self,tile):
        '''
        pram: tile - int
        return: tuple (i,j) for the position of the tile; None if not found
        '''
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == tile:
                    return (i,j)
        return None
    def __eq__(self,other):
        '''
        pram: other - State
        return: True if the states are equal, False otherwise
        '''
        if (self.pos[0]!=other.pos[0] or self.pos[1]!=other.pos[1]):
            return False
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] != other.grid[i][j]:
                    return False
        return True
    
    def __hash__(self):
        """
        Allow State objects to be used as keys in dictionaries or sets.
        """
        # We need an immutable representation of the grid for hashing.
        # A string is a simple and effective way to do this.
        return hash(str(self.grid))
    
    def mDist(self,other):
        '''
        pram: other - State
        return: the Manhattan distance between the two states
        '''
        result=0
        for t in range(1,self.size**2):
            p1 = self.tPos(t)
            p2 = other.tPos(t)
            if p1 != None and p2 != None:
                result+=abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        return result
    
def tester():
    grid = [[1,2,3],[4,0,5],[6,7,8]]
    st = State(grid)
    
    print(st)
    for move,next_state in st.move():
        print(move)
        print(next_state)
        
        
    print("second test")
    
    grid2 = [[1,2,3],[4,5,0],[6,7,8]]
    sa = State(grid2)
   
    for move,next_state in sa.move():
        print(move)
        print(next_state)
    


if __name__ == "__main__":
    tester()
    
