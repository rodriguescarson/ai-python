from queue import PriorityQueue
graph = {
    'A': [['B', 3], ['C', 2]],
    'B': [['A', 5], ['C', 2], ['D', 2], ['E', 3]],
    'C': [['A', 5], ['B', 3], ['F', 2], ['G', 4]],
    'D': [['H', 1], ['I', 99]],
    'F': [['J', 99]],
    'G': [['K', 99], ['L', 3]],
    'E': [],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
}
# nodes = input("Enter the nodes: ").split()
# graph = dict.fromkeys(nodes, 0)

# for i in graph.keys():
#     print("Enter the neighbours of ", i, ": ", end="")
#     neighbours = input().split()
#     print("Enter the heuristic of neighbours of ", i, ": ", end="")
#     heuristic = input().split()
#     graph[i] = zip(neighbours, heuristic)

q = PriorityQueue()

visited = []


def bestforsearch(graph, node, goal):
    q.put(node[::-1])
    visited.append(node)
    while q:
        m = q.get(0)
        print(m[::-1])
        if m[1] == goal:
            return
        for neighbor in graph[m[1]]:
            if neighbor not in visited:
                visited.append(neighbor)
                q.put(neighbor[::-1])


bestforsearch(graph, ('A', 0), 'H')
