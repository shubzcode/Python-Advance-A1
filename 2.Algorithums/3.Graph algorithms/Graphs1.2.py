# Breadth-first search: A graph traversal algorithm that starts at 
# a vertex and explores all of its neighbors before exploring any of their neighbors.
# Method 2
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(self.graph[vertex])

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS traversal starting from vertex 2:")
g.bfs(2)
