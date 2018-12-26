import heapq


def dijkstra(begin, graph, dist, duracao):
    dist[begin] = 0
    queue = []
    heapq.heappush(queue, (0, begin))

    while queue:
        no = heapq.heappop(queue)

        if int(no[0]) > dist[no[1]]:
            continue

        for v in graph[no[1]]:

            a = 0
            if(no[0] != 0):
                a = v[0]
                while (a < no[0]):
                    a += v[0]

            if dist[v[1]] > a + duracao:
                dist[v[1]] = a + duracao
                heapq.heappush(queue, ([dist[v[1]], v[1]]))

    return dist


vzs = int(input())
c = 1

while (c <= vzs):

    dic = {}
    cidade = {}

    a = 0

    enter = input().split(' ')
    origem1 = enter[0]
    destino1 = enter[1]
    duracao = int(enter[2])
    n = int(enter[3])

    dic[origem1] = a
    a += 1
    dic[destino1] = a
    a += 1
    cidade[dic[origem1]] = []
    cidade[dic[destino1]] = []

    for i in range(n):

        enter = input().split(' ')
        origem = enter[0]
        destino = enter[1]
        custo = int(enter[2])

        if origem not in dic:
            dic[origem] = a
            a += 1
        if destino not in dic:
            dic[destino] = a
            a += 1

        if dic[origem] not in cidade:
            cidade[dic[origem]] = [[custo, dic[destino]]]
        else:
            cidade[dic[origem]].append([custo, dic[destino]])

        if dic[destino] not in cidade:
            cidade[dic[destino]] = []

    dists = [999999] * a

    dists = dijkstra(dic[origem1], cidade, dists, duracao)

    if(dists[dic[destino1]] < 999998):
        print("Caso #"+str(c)+": "+str(dists[dic[destino1]])+" anticalmas")
    else:
        print("Caso #" + str(c) + ": Destino inalcancavel")
    c += 1