import heapq

def dijkstra(begin, graph, dist, path):

    dist[begin] = 0

    queue = []

    heapq.heappush(queue,(0,begin))

    while queue:
        no = heapq.heappop(queue)
        if int(no[0]) > dist[no[1]]:
            continue
        for v in graph[no[1]]:
            if dist[v[1]] > no[0] + v[0]:
                path[v[1]] = no[1]
                dist[v[1]] = no[0] + v[0]
                heapq.heappush(queue,([dist[v[1]], v[1]]))

    return dist,path

while(True):
    graph = {}

    enter = input().split()
    n_nos = n_nodes = int(enter[0])
    n_edgs = int(enter[1])

    if(n_nos == n_edgs == 0):
        break

    enter = input().split()
    origem = int(enter[0])
    save_d = destino = a = int(enter[1])

    dists = [999999] * (n_nos+1)
    path = [-1] * (n_nos+1)
    while n_nos>=0:
        graph[n_nos] = []
        n_nos-=1

    while(n_edgs>0):
        enterk = [int(i) for i in input().split()]
        n_edgs-=1
        graph[enterk[0]].append([enterk[2], enterk[1]])

    dists,path = dijkstra(origem,graph,dists,path)

    print_f = pr_d = dists[save_d]
    m = -9
    lista_fim = [a]
    while(a != -1):
        m = path[a]
        lista_fim.append(m)
        a = m

    i = 1
    a = lista_fim[i]
    while(a != -1):
        list_inf = graph[a]
        for x in list_inf:
            if(x[1] == destino):
                x[0] = 999999
                break
        destino = a
        i+=1
        a = lista_fim[i]

    dists = [999999] * (n_nodes+1)
    dists,path = dijkstra(origem,graph,dists,path)
    print_f = dists[save_d]
    print(print_f)