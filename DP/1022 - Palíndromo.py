def dp(word):
    size = len(word)
    table = [0] * size
    for x in range(size):
        table[x] = [0] * size
        table[x][x] = 1

    comp = 2
    while comp <= size:
        i = 0
        while i < size - comp + 1:
            j = i + comp - 1
            if comp == 2 and word[i] == word[j]:
                table[i][j] = 2
            elif word[i] == word[j]:
                table[i][j] = table[i + 1][j - 1] + 2
            else:
                table[i][j] = table[i + 1][j] \
                    if table[i + 1][j] > table[i][j - 1] \
                    else table[i][j - 1]
            i += 1
        comp += 1

    try:
        return table[0][size - 1]

    except:
        return 0


n = int(input())
while n > 0:
    word = list(input())

    print(dp(word))

    n -= 1
