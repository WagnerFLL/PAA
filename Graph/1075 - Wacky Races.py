import heapq
import sys
sys.setrecursionlimit(10000)

ans = []
graph = {}

def dijkstra(begin, graph, dist):

    dist[begin] = 0
    queue = []
    heapq.heappush(queue, (0, begin))

    while queue:
        no = heapq.heappop(queue)
        if int(no[0]) > dist[no[1]]:
            continue

        for v in graph[no[1]]:
            if dist[v[0]] > no[0] + v[1]:
                dist[v[0]] = no[0] + v[1]
                heapq.heappush(queue, ([dist[v[0]], v[0]]))

    return dist

def findBridge(u, visited, father, minor, discovery):
    visited[u] = True
    minor[u] = discovery[u] = graph["order"]

    graph["order"] += 1

    for node in graph[u]:
        if not visited[node[0]]:
            father[node[0]] = u
            findBridge(node[0], visited, father, minor, discovery)
            minor[u] = minor[u] if minor[u] < minor[node[0]] else minor[node[0]]

            if minor[node[0]] > discovery[u]:
                ans.append(node[0])
                ans.append(u)

        elif father[u] != node[0]:
            minor[u] = minor[u] if minor[u] < discovery[node[0]] else discovery[node[0]]


def allBridges(n):
    visited = [False] * (n)
    discovery = [9999999] * (n)
    minor = [9999999] * (n)
    father = [-1] * (n)
    for i in range(n):
        if not visited[i]:
            findBridge(i, visited, father, minor, discovery)

enter = input().split()
n = int(enter[0])
edges = int(enter[1])

for i in range(n+1):
    graph[i] = []

for i in range(edges):
    enter = input().split()
    graph[int(enter[0])].append( (int(enter[1]),int(enter[2])) )
    graph[int(enter[1])].append( (int(enter[0]),int(enter[2])) )
graph["order"] = 0

dist = [99999999] * (n+1)
dist = dijkstra(1,graph,dist)
allBridges(n+1)

if len(ans) == 0:
    print("It's not possible")
else:
    a = b = 9999999
    for x in ans:
        a = dist[x]
        if a < b:
            b = a
    print("It's possible with distance "+str(b))