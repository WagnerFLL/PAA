def moduleDif(a,b):
    a -= b
    if(a>=0):
        return a
    return -a

def search(lista,n,money):

    exactj = 0
    exacti = money
    i = 0

    while(i<n):
        j = i+1

        while(j<n):

            if((int(lista[i])+int(lista[j]) == money) and (moduleDif(int(lista[i]),int(lista[j]) > moduleDif(exactj,exacti)))):
                exacti = int(lista[i])
                exactj = int(lista[j])

            j+=1

        i+=1

    if(exacti > exactj):
        temp = exacti
        exacti = exactj
        exactj = temp

    print('Peter should buy books whose prices are %d and %d.' %(exacti , exactj))
    print()

while(True):
    try:
        numberBooks = int(input())
        priceBooks = input().split(' ')
        money = int(input())
        input()

        search(priceBooks,numberBooks,money)
    except EOFError:
        break