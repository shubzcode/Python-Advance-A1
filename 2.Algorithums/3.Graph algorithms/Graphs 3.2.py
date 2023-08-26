# Dijkstra's algorithm: An algorithm for finding the shortest 
# path between two vertices in a weighted graph.
# Method 2
import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
    
    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

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

start_vertex = 'A'
shortest_distances = g.dijkstra(start_vertex)

for vertex, distance in shortest_distances.items():
    print(f"Shortest distance from {start_vertex} to {vertex}: {distance}")
