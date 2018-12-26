def binary_search(lista, inicio, fim, busca, l):
    meio = int((fim + inicio) / 2)

    if (meio >= l):
        return -1

    if (lista[meio] == busca):
        return meio

    if ((fim == inicio) or (meio >= fim)):
        return -1

    if (lista[meio] > busca):
        return binary_search(lista, inicio, meio - 1, busca, l)
    else:
        return binary_search(lista, meio + 1, fim, busca, l)


enter = [int(i) for i in input().split(' ')]
linha = enter[0]
coluna = enter[1]

lista = []

for x in range(linha):
    enter = input().split(' ')
    [lista.append(int(i)) for i in enter]

n_buscas = int(input())
buscas = [int(i) for i in input().split(' ')]

for i in buscas:

    posicao = binary_search(lista,0,linha*coluna,i,linha*coluna) +1

    if(posicao != 0):
        if(posicao % coluna == 0):
            p_linha = int(posicao / coluna)
        else:
            p_linha = int(posicao / coluna) + 1
        p_coluna = int(posicao % coluna)
        if(p_coluna == 0):
            p_coluna = coluna
        print("YES WITH "+str(p_linha)+" AND "+str(p_coluna))
    else:
        print("NO")