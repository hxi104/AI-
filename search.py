# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 12:50:19 2025

@author: harry
"""

from tiles import State

def dfs(start,end):
    stack = [(start,[])] #starting state and empty move list
    visited = set() #stores explored states
    while stack:
        state,path = stack.pop() #takes last state DFS = last in first out
        if state.grid == end.grid: #compare grids
            return path  # solution found
        visited.add(str(state.grid)) # convert grid to str and add to visited
        
        #explore all moves
        for move,next_state in state.move():
            if str(next_state.grid) not in visited:
                stack.append((next_state,path+[move]))
    return None
def dfs_r(start,end):
    visited = set()
    path = []
    def recurse(state):
        if state.grid == end.grid:
            return path

        visited.add(str(state.grid))

        for move, next_state in state.move():
            if str(next_state.grid) not in visited:
                path.append(move)
                result = recurse(next_state)
                if result is not None:   # found goal
                    return result
                path.pop()               # backtrack if dead end

        return None

    return recurse(start)
    
    
    
    
    
    
if __name__ == "__main__":
    start_grid = [[1,2,3],
                  [4,0,5],
                  [6,7,8]]
    
    goal_grid  = [[1,2,3],
                  [4,5,0],
                  [6,7,8]]

    start = State(start_grid)
    goal = State(goal_grid)

    path = dfs(start, goal)
    if path:
        print("DFS Path found!")
        print("moves:",path)
    else:
        print("no path")
        

    path_r = dfs_r(start,goal)
    if path_r:
        print("recursive DFS path found")
        print("moves:",path)