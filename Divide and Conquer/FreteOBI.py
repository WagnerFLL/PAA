import heapq

def dijkstra(begin, graph, dist):

    dist[begin] = 0

    queue = []

    heapq.heappush(queue,(0,begin))

    while queue:
        no = heapq.heappop(queue)
        if int(no[0]) > dist[no[1]]:
            continue

        for v in graph[no[1]]:
            if dist[v[1]] > no[0] + v[0]:
                dist[v[1]] = no[0] + v[0]
                heapq.heappush(queue,([dist[v[1]], v[1]]))

    return dist

nos, arestas = map(int, input().split(' '))

graph = {}

for j in range(arestas):
    u, v, c = map(int, input().split(' '))

    if u not in graph:
        graph[u] = [[c, v]]
    else:
        graph[u].append([c, v])

    if v not in graph:
        graph[v] = [[c, u]]
    else:
        graph[v].append([c, u])

dists = [100001]*(nos+1)

dists = dijkstra(1,graph,dists)
print(dists)