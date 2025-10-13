# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 12:50:19 2025

@author: harry
"""

from tiles import State
from heapq import heappush, heappop
import itertools

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
def dfs_r(start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # Base case: goal reached
    if start.grid == goal.grid:
        return path

    # Create an immutable representation for visited states
    grid_key = str(start.grid)
    visited.add(grid_key)

    # Explore possible moves
    for move, new_state in start.move():
        new_key = str(new_state.grid)
        if new_key not in visited:
            result = dfs_r(new_state, goal, visited, path + [move])
            if result is not None:
                return result  # stop as soon as a valid path is found

    return None
    
    

def aStar(start, end):
    frontier = []
    # --- ADD A COUNTER ---
    tie_breaker = itertools.count() # Creates a counter that starts at 0

    # The first item needs the counter too
    heappush(frontier, (0, next(tie_breaker), start)) 
    
    came_from = {start: None}
    move_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        # Unpack the counter, but you don't need to use it
        _, _, current = heappop(frontier) 

        if current == end:
            # reconstruct path
            path = []
            while move_from[current] is not None:
                path.append(move_from[current])
                current = came_from[current]
            path.reverse()
            return path

        # Explore possible moves
        for move, next_state in current.move():
            new_cost = cost_so_far.get(current, 0) + 1 # Use .get() for safety
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = new_cost + next_state.mDist(end)
                
                # --- ADD THE COUNTER TO THE PUSHED TUPLE ---
                heappush(frontier, (priority, next(tie_breaker), next_state))
                
                came_from[next_state] = current
                move_from[next_state] = move

    return None
    



if __name__ == "__main__":
    start_grid = [[1,2,3],
                  [4,0,5],
                  [6,7,8]]
    
    goal_grid  = [[1,2,3],
                  [0,4,5],
                  [6,7,8]]

    start = State(start_grid)
    goal = State(goal_grid)
    
    
    print("=== DFS ===")
    path = dfs(start, goal)
    print("DFS path:", path)
    
    print("\n=== Recursive DFS ===")
    path_r = dfs_r(start, goal)
    print("Recursive DFS path:", path_r)
    
    print("\n=== A* ===")
    path_a = aStar(start, goal)
    print("A* path:", path_a)
    

    