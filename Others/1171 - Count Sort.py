pogCountList = [0]*10000000

lista = [int(i) for i in input().split(' ')]

n = len(lista)

for i in lista:
    pogCountList[int(i)] += 1

i = 0
a = 0
while(a < n):
    qtd = pogCountList[i]
    for x in range(qtd):
        print(i)
        a += 1
    i += 1