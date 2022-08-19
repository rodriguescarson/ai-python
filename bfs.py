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

queue = []
visted = []


def bfs(graph, node, goal):
    if(goal == node):
        print("Root node is goal node")
        return True
    visted.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        if m == goal:
            print(m)
            return True
        else:
            print(m)
        for neighbor in graph[m]:
            if neighbor not in visted:
                visted.append(neighbor)
                queue.append(neighbor)


if(bfs(graph, '5', '2')):
    print("Goal node found")
else:
    print("Goal node not found")
