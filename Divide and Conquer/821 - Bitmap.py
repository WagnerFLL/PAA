def bitmap(matriz, li, lf, ci, cf, im):

    try:

        if ((li == lf) or (ci == cf)):
            return 0

        freq = matriz[li][ci]

        flag = 0

        i = li
        while (i < lf):

            j = ci

            while (j < cf):
                if (freq != matriz[i][j]):
                    flag = 1
                    break
                j += 1

            i += 1

        if (flag):

            if ((im[0] % 50 == 0) and (im[0] > 0)):
                print()
            print("D", end="")
            im[0] += 1

            if ((lf - li == 1) and (cf - ci == 1)):
                return 0

            meiol = meioc = 0

            if ((ci + cf) % 2 == 0):
                meioc = int((ci + cf) / 2)
            else:
                meioc = int((ci + cf) / 2) + 1

            if ((li + lf) % 2 == 0):
                meiol = int((li + lf) / 2)
            else:
                meiol = int((li + lf) / 2) + 1

            bitmap(matriz, li, meiol, ci, meioc, im)
            bitmap(matriz, li, meiol, meioc, cf, im)
            bitmap(matriz, meiol, lf, ci, meioc, im)
            bitmap(matriz, meiol, lf, meioc, cf, im)

        else:
            if ((im[0] % 50 == 0) and (im[0] > 0)):
                print()
            print(freq, end="")
            im[0] += 1

    except:

        print("", end="")


n = int(input())

while (n > 0):
    enter = input().split()
    linha = int(enter[0])
    coluna = int(enter[1])

    matriz = []

    for i in range(linha):
        enter = list(input())
        matriz.append(enter)

    l = []
    l.append(0)
    bitmap(matriz, 0, linha, 0, coluna, l)
    print()
    n -= 1