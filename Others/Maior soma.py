def max(num1, num2):
    if num1 > num2:
        return num1
    return num2

def maior_soma(lista,inicio,fim):

    meio = int((fim+inicio)/2)
    maxD = maxL = soma = 0
    i = meio+1

    if(inicio == fim):
        if(lista[inicio] >= 0):
            return lista[inicio]
        return 0

    while(i <= fim):
        soma += lista[i]
        if(soma > maxD):
            maxD = soma
        i+=1

    soma = 0
    i = meio

    while(i >= inicio):
        soma += lista[i]
        if(soma > maxL):
            maxL = soma
        i-=1

    return max(
                max(maior_soma(lista,inicio,meio),
                    maior_soma(lista,meio+1,fim))
               ,maxD+maxL)

n = int(input("Quantos elementos terá a lista?"))

lista = []

for i in range(n):
    lista.append(int(input()))

n = maior_soma(lista,0,n-1)

print(n)