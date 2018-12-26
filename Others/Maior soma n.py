def max_sum(lista):

    soma = max = 0

    for i in lista:
        soma += i
        if(soma > max):
            max = soma
        if(soma < 0):
            soma = 0

    return soma

n = int(input("Quantos valores?"))

lista = []

for i in range(n):
    enter = int(input(" - "))
    lista.append(enter)

n = max_sum(lista)