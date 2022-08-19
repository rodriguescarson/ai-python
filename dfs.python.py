import sys
# graph = {
#     'A': ['D', 'B'],
#     'B': ['C', 'F'],
#     'C': ['G', 'E', 'H'],
#     'G': ['E', 'H'],
#     'E': ['B', 'F'],
#     'F': ['A'],
#     'D': ['F'],
#     'H': ['A'],
# }

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': [],
}

# nodes = input("Enter the nodes: ").split()
# graph = dict.fromkeys(nodes, 0)

# for i in graph.keys():
#     print("Enter the neighboursof ", i, ": ", end="")
#     graph[i] = input().split()

visited = []


def dfs(graph, node, goal):
    if(node == goal):
        print("Root node is goal node")
        return
    visited.append(node)
    m = visited[-1]
    print(m)
    for neighbor in graph[m]:
        if neighbor not in visited:
            if neighbor == goal:
                print(neighbor)
                print("Goal node found")
                sys.exit(0)
            else:
                dfs(graph, neighbor, goal)


dfs(graph, '5', '5')
