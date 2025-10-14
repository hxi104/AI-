# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 12:50:19 2025

@author: harry
"""

from tiles import State
from heapq import heappush, heappop
import itertools
import timeit

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
    
def _depth_limited_dfs(start,end,limit,path,path_set):
    if start.grid == end.grid:
        return path
    if limit == 0:
        return None
    for move, new_state in start.move():
        new_key = str(new_state.grid)
        if new_key in path_set:
            continue
        path_set.add(new_key)
        result = _depth_limited_dfs(new_state, end, limit-1, path+[move], path_set)
        if result is not None:
            return result
        path_set.remove(new_key)
    return None

def id_dfs(start, goal, max_depth=50):
    if start.grid == goal.grid:
        return []
    for depth in range(max_depth + 1):
        start_key = tuple(tuple(row) for row in start.grid)
        path_set = {start_key}
        result = _depth_limited_dfs(start, goal, depth, [], path_set)
        if result is not None:
            return result
    return None


def compare_algorithms(start, end, number=5):
    """
    Compare performance of DFS, Recursive DFS, ID-DFS, and A* algorithms
    using timeit for more accurate timing.

    Args:
        start, end: State instances for the puzzle.
        number: how many times each algorithm runs (default 5).
    """

    algorithms = [
        ("DFS (iterative)", dfs),
        ("DFS (recursive)", dfs_r),
        ("ID-DFS", id_dfs),
        ("A*", aStar)
    ]

    print("\n=== Comparing Search Algorithms ===")
    print(f"Start: {start.grid}")
    print(f"Goal : {end.grid}")
    print("-----------------------------------------")
    print(f"{'Algorithm':<20} {'Found':<8} {'PathLen':<8} {'Avg Time (s)':<12}")
    print("-----------------------------------------")

    for name, func in algorithms:
        try:
            # Define a wrapper so timeit can call the algorithm
            def run_func():
                return func(start, end)

            # Measure total time for `number` runs
            total_time = timeit.timeit(run_func, number=number)
            avg_time = total_time / number

            # Run once more to capture actual output (not timed)
            path = func(start, end)
            found = "Yes" if path is not None else "No"
            length = len(path) if path is not None else "-"

            print(f"{name:<20} {found:<8} {length!s:<8} {avg_time:<12.6f}")

        except Exception as e:
            print(f"{name:<20} Error: {str(e)}")

    print("-----------------------------------------\n")

    
    
    
    
    

if __name__ == "__main__":
    start_grid = [[1,2,3],
                  [4,0,5],
                  [6,7,8]]
    
    goal_grid  = [[1,2,3],
                  [4,5,6],
                  [7,8,0]]

    start = State(start_grid)
    goal = State(goal_grid)
    
    
    compare_algorithms(start, goal)
    

    