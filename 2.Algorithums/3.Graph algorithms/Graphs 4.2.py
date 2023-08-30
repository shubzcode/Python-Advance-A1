# Prim's algorithm: An algorithm for finding the minimum spanning tree of a weighted graph.
#method 2 
import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def prim(self):
        minimum_spanning_tree = []
        visited = set()
        start_vertex = list(self.graph.keys())[0]
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_weight, current_vertex = heapq.heappop(priority_queue)
            if current_vertex in visited:
                continue
            visited.add(current_vertex)
            
            for neighbor, weight in self.graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, neighbor))
                    minimum_spanning_tree.append((current_vertex, neighbor, weight))
        
        return minimum_spanning_tree

# Example usage
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 5)
g.add_edge('B', 'D', 10)
g.add_edge('C', 'D', 3)
g.add_edge('D', 'E', 7)
g.add_edge('E', 'C', 8)
g.add_edge('E', 'A', 1)

minimum_spanning_tree = g.prim()

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} --({edge[2]})-- {edge[1]}")
