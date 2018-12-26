import heapq

def dijkstra(begin, graph, dist, destino, visits):

    dist[begin] = 0
    visits[begin] = 1

    queue = []

    heapq.heappush(queue,(0,begin))

    while queue:
        no = heapq.heappop(queue)

        if (dist[destino] < 99999) and (visits[destino] < 2):
            break

        for v in graph[no[1]]:
            visits[ no[1] ] += 1
            if no[0]%3 == v[0]:
                dist[v[1]] = 99999

            else:
                dist[v[1]] = no[0] + 1
                heapq.heappush(queue,([dist[v[1]], v[1]]))

    return dist

enter = input().split(' ')

n_no = int(enter[0])
origem1 = int(enter[1])
destino1 = int(enter[2])
n_arestas = int(enter[3])

cidade = {}

for i in range(n_no):
    cidade[i] = []

dists = [999999] * n_no
visits = [0] * n_no

for i in range(n_arestas):

    enter = input().split(' ')
    cidade[ int(enter[0]) ].append( [int(enter[2]), int(enter[1])] )

# print(cidade)
dists = dijkstra( origem1, cidade, dists, destino1, visits )
print(dists[destino1])