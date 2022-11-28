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

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth):
        result = dls(graph, start, goal, depth)
        if result != "cutoff":
            return result
    return "cutoff"

def dls(graph, start, goal, depth):
    if start == goal:
        return [start]
    elif depth == 0:
        return "cutoff"
    else:
        cutoff_occurred = False
        for node in graph[start]:
            result = dls(graph, node, goal, depth - 1)
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                result.insert(0, start)
                return result
        if cutoff_occurred:
            return "cutoff"
        else:
            return "failure"

def print_path(path):
    if path == "cutoff":
        print("cutoff")
    elif path == "failure":
        print("failure")
    else:
        for node in path:
            print(node, end=" ")
        print()

if __name__ == "__main__":
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")
    while True:
        max_depth = int(input("Enter the max depth: "))
        if max_depth <= 10 and max_depth >= 0:
            break
        else:
            print("Please enter a value between 0 and 10")
    path = iddfs(graph, start, goal, max_depth)
    print_path("Iterative deepening depth first search result: " + str(path))