def max_sum(lista):

    soma = inicio = final = i = max = auxj = 0
    size = len(lista)

    while(i < size):
        soma += lista[i]
        if(soma == max):
            if((i - auxj) > final-inicio):
                final = i
                inicio = auxj
        if(soma > max):
            max = soma
            final = i
            inicio = auxj
        if(soma < 0):
            soma = 0
            auxj = i + 1

        i += 1

    if(max == 0):
        print("nenhum")
    else:
        print(inicio + 1, final + 1)
    print()


n = int(input())
i = 0

while(n != 0):
    lista = []
    i += 1
    while(n>0):
        pogList = input().split(' ')
        lista.append(int(pogList[0])-int(pogList[1]))
        n -= 1
    print("Teste",i)
    max_sum(lista)
    n = int(input())