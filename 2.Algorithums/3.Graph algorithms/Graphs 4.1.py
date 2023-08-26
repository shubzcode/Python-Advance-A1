# Prim's algorithm: An algorithm for finding the minimum spanning tree of a weighted graph.
# Method 1
    
import heapq
def prim(graph):
    visited = set()
    mst = set()
    pq = []
    pq.append((0, "A"))

    while pq:
        _, vertex = heapq.heappop(pq)
        visited.add(vertex)
        mst.add((vertex, neighbor))

        for neighbor, weight in graph[vertex].items():
            if neighbor not in visited and weight < min(weight for vertex, weight in mst):
                heapq.heappush(pq, (weight, neighbor))


def main():
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"C": 2, "D": 1},
        "C": {},
        "D": {"E": 4},
        "E": {},
    }

    prim(graph)
    mst = set()
    mst.add((vertex, neighbor))



    print("The minimum spanning tree is", mst)


if __name__ == "__main__":
    main()
