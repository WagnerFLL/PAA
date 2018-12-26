import sys

sys.setrecursionlimit(10000)

graph = {}


def findBridge(u, visited, father, minor, discovery, ans):
    visited[u] = True
    minor[u] = discovery[u] = graph["order"]
    children = 0
    graph["order"] += 1

    for node in graph[u]:
        if not visited[node]:
            children += 1
            father[node] = u
            findBridge(node, visited, father, minor, discovery, ans)
            minor[u] = minor[u] if minor[u] < minor[node] else minor[node]

            if father[u] == -1 and children > 1:
                ans[u] = True
            elif father[u] != -1 and minor[node] >= discovery[u]:
                ans[u] = True

        elif father[u] != node:
            minor[u] = minor[u] if minor[u] < discovery[node] else discovery[node]


def allBridges(n):
    visited = [False] * (n)
    discovery = [9999999] * (n)
    minor = [9999999] * (n)
    father = [-1] * (n)
    ans = [False] * n
    for i in range(n):
        if not visited[i]:
            findBridge(i, visited, father, minor, discovery, ans)
    return ans


n = int(input())
while n != 0:

    for i in range(n + 1):
        graph[i] = []

    for i in range(n):
        enter = input().split()
        if int(enter[0]) == 0:
            break
        else:
            for x in enter[1:]:
                graph[int(enter[0])].append(int(x))
                graph[int(x)].append(int(enter[0]))

    graph["order"] = 0

    ans = allBridges(n + 1)
    count = 0

    for x in ans:
        if x:
            count += 1
    print(count)
    n = int(input())