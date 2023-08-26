# Depth-first search: A graph traversal algorithm that explores 
# a vertex and then explores its neighbors in a recursive manner.
#method 1
def depth_first_search(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                stack.append(neighbor)


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

    depth_first_search(graph, start)

    visited = visited
    print("The visited vertices are", visited)


if __name__ == "__main__":
    main()
