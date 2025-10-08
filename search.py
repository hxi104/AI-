# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 12:50:19 2025

@author: harry
"""

from tiles import State

def dfs(start,end):
    stack = [(start,[])] #starting state and emply move list
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

if __name__ == "__main__":
    start_grid = [[1,2,3],
                  [4,0,5],
                  [6,7,8]]
    
    goal_grid  = [[1,2,3],
                  [4,5,6],
                  [7,8,0]]

    start = State(start_grid)
    goal = State(goal_grid)

    path = dfs(start, goal)
    if path:
        print("Path found!")
        print("moves:",path)
        print("\nReplaying moves:")
        current = start
        for move in path:
            current = State.apply_move(current, move)
            print(f"\nAfter move: {move}")
            print(current)
    else:
        print("no path")