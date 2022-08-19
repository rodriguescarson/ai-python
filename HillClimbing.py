from operator import itemgetter

graph = {
    'A': [['B', 3], ['C', 6], ['D', 3]],
    'B': [],
    'C': [['M', 17]],
    'D': [['E', 8], ['F', 4], ['G', 5]],
    'E': [['H', 5], ['I', 3]],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'M': []
}

# nodes = input("Enter the nodes: ").split()
# graph = dict.fromkeys(nodes, 0)

# for i in graph.keys():
#     print("Enter the neighbours of ", i, ": ", end="")
#     neighbours = input().split()
#     print("Enter the heuristic of neighbours of ", i, ": ", end="")
#     heuristic = input().split()
#     graph[i] = zip(neighbours, heuristic)

visited = []


def hillclimbing(graph, node):
    visited.append(node)
    neighbours = sorted(graph[node[0]], key=itemgetter(1))
    if neighbours == []:
        return
    bestneighbour = neighbours[-1]
    if node[1] > bestneighbour[1]:
        return
    hillclimbing(graph, bestneighbour)


hillclimbing(graph, ['A', 2])
print("Traversal path: ", visited)
