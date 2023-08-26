# Depth-first search: A graph traversal algorithm that explores 
# a vertex and then explores its neighbors in a recursive manner.
# method 2
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 4)
g.add_edge(3, 3)

print("DFS traversal starting from vertex 2:")
visited_set = set()
g.dfs_recursive(2, visited_set)
