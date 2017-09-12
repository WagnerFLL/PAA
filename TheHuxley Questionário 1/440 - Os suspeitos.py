from queue import *

def bfs(graph, n_nodes):

    infected = 1

    queue = Queue()
    queue.put(0)

    visited = [False] * n_nodes
    visited[0] = True

    while(not queue.empty()):
        node = queue.get()

        for x in graph[node]:
            if(not visited[x]):
                visited[x] = True
                infected += 1
                queue.put(x)

    return infected


def add_edges(graph, nodes):

    x = nodes[0]
    nodes.pop(0)

    while(nodes):
        graph[0].append(x)
        nodes.pop(0)
        
while (True):

    enter = input().split(' ')
    n_node = int(enter[0])
    n_groups = int(enter[1])

    if(n_groups == 0 and  n_node == 0):
        break

    graph = [[]]
    for x in range(0, n_node):
        graph.append([])

    for x in range(0, n_groups):
        enter = [int(i) for i in input().split()]
        enter.pop(0)
        add_edges(graph, enter)

    print(bfs(graph, n_node))