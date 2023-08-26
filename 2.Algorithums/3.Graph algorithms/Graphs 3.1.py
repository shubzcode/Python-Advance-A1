# Dijkstra's algorithm: An algorithm for finding the shortest 
# path between two vertices in a weighted graph.
# Method 1
from cv2 import distanceTransform


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    visited = set()
    pq = []
    pq.append((0, start))

    while pq:
        _, vertex = pq.pop(pq)
        visited.add(vertex)

        for neighbor, weight in graph[vertex].items():
            if neighbor not in visited and distances[neighbor] > distances[vertex] + weight:
                distances[neighbor] = distances[vertex] + weight
                pq.push(pq, (distances[neighbor], neighbor))


def main():
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"C": 2, "D": 1},
        "C": {},
        "D": {"E": 4},
        "E": {},
    }

    start = "A"

    dijkstra(graph, start)

    print("The shortest distances from", start, "are", distanceTransform)


if __name__ == "__main__":
    main()
