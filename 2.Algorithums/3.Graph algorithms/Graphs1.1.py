# Breadth-first search: A graph traversal algorithm that
# starts at a vertex and explores all of its neighbors before exploring any of their neighbors.
# Method 1
def breadth_first_search(graph, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": [],
    }

    start = "A"

    breadth_first_search(graph, start)

    print("The visited vertices are", visited())

def visited():
    return visited


if __name__ == "__main__":
    main()
