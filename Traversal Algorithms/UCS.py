import heapq

graph = {
    'A': {'D': 43, 'O': 151},
    'B': {'G': 171},
    'C': {'B': 171, 'D': 126},
    'D': {'F': 111, 'M':200, 'O':136},
    'E': {'A': 133, 'L': 110},
    'F': {'G': 88, 'H': 130},
    'G': {'C': 140, 'D': 123},
    'H': {'N': 80},
    'I': {'A': 109, 'C': 102},
    'J': {'E': 105, 'I': 172, 'K': 146},
    'K': {'E': 146, 'L': 152},
    'L': {'O': 97},
    'M': {'N': 67},
    'N': {},
    'O': {'M': 100}
    }

def ucs_path(graph, start, end):
    visited = set()
    queue = [(0, start, [])]
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return ("Uniform Cost Search: " + str(path) + "\nCost: " + str(cost))
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    return None

start = input("Enter start node: ")
end = input("Enter end node: ")
print(ucs_path(graph, start, end))