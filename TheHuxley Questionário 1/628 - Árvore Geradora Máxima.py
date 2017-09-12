import queue as Q

def convert(queue):

    lista = []
    while queue:
        lista.append(queue.get())
        if(queue.empty()):
            return lista

t = int(input())

while(t > 0):

    enter = input().split()
    n_no = int(enter[0])
    n_aresta = int(enter[1])

    queue = Q.PriorityQueue()


    for i in range(n_aresta):
        enter = input().split()
        queue.put((-1 * int(enter[2]),int(enter[0]),int(enter[1])))

    graph = {}
    lista = []
    lista = convert(queue)

    current = lista[0]
    graph[current[1]] = [[current[0],current[2]]]
    graph[current[2]] = [[current[0], current[1]]]
    print(lista)
    qtd = 1
    val = current[0]
    print(current)
    lista.remove(current)

    while(qtd < n_no-1):

        for current in lista:

            if (current[1] not in graph) and (current[2] in graph):
                graph[current[2]].append([current[0], current[1]])
                graph[current[1]] = [[current[0], current[2]]]
                val += current[0]
                qtd += 1
                print(current)
                lista.remove(current)
                break

            elif (current[2] not in graph) and (current[1] in graph):
                graph[current[1]].append([current[0], current[2]])
                graph[current[2]] = [[current[0], current[1]]]
                val += current[0]
                qtd += 1
                print(current)
                lista.remove(current)
                break

    print(val * -1)

    t -= 1