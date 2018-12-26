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
            if dist[v] > no[0] + 1:
                dist[v] = no[0] + 1
                heapq.heappush(queue,([dist[v], v]))

    return dist

n = int(input())
vzs = 1

print("SHIPPING ROUTES OUTPUT")

while(vzs <= n):

    print()
    print("DATA SET  "+str(vzs))
    print()

    enter = input().split()
    n_arestas = int(enter[1])
    n_buscas = int(enter[2])

    oceano = {}
    dict = {}

    a = 0
    enter = input().split()
    for i in enter:
        dict[i] = a
        oceano[a] = []
        a += 1

    for i in range(n_arestas):
        enter = input().split()

        oceano[dict[enter[0]]].append(dict[enter[1]])
        oceano[dict[enter[1]]].append(dict[enter[0]])

    dists = [9999] * a
    copy_dists = dists[:]

    for i in range(n_buscas):
        dists = copy_dists[:]
        enter = input().split()
        dists = dijkstra( dict[enter[1]], oceano, dists )
        # print(enter[1],end=" ")
        # print(enter[2])
        # print(dists)
        saida = 100 * int(enter[0]) * dists[ dict[enter[2]] ]

        if(dists[ dict[enter[2]] ] > 999 ):
            print("NO SHIPMENT POSSIBLE")
        else:
            print("$"+str(saida))

    vzs += 1

print()
print("END OF OUTPUT")