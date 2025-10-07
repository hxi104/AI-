# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 10:41:29 2025

@author: harry
"""

def dfs(graph, start):
    visited,stack=[],[start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            adj=[u for u in graph[vertex].copy() if u not in visited]
            stack.extend(adj)
    return visited

graph_data = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C', 'E']
    }
print(dfs(graph_data, 'D'))

def dfs_path(graph,start,goal):
    stack=[(start,[start])]
    while stack:
        vertex,path=stack.pop()
        #obtain remaining adjacent vertices
        adj=[u for u in graph[vertex].copy() if u not in path]
        for v in adj: #next vertex to explore
            if v==goal:
                return path+[v]
            else:
                stack.append((v,path+[v]))
                
def dfs_paths(graph,start,goal):
    stack=[(start,[start])]
    while stack:
        vertex,path=stack.pop()
        #obtain remaining adjacent vertices
        adj=[u for u in graph[vertex].copy() if u not in path]
        for v in adj:
            new_path = path + [v]
            if v==goal:
                yield new_path
            else:
                stack.append((v,new_path))
                
#one path from one vertex to another
print(dfs_path(graph_data,'A','F'))
print(list(dfs_paths(graph_data,'A','F')))