def dp(lista, n):
    sumk = sum(lista)
    mid = int(sumk / 2) + 1

    if sumk % 2 != 0:
        return False

    memo = [[False for x in range(n + 1)] for x in range(mid)]

    for x in range(n + 1):
        memo[0][x] = True

    for i in range(mid):
        for j in range(n + 1):
            memo[i][j] = memo[i][j - 1]
            if i >= lista[j - 1]:
                memo[i][j] = memo[i][j] or memo[i - lista[j - 1]][j - 1]

    return memo[mid - 1][n]


enter = [int(x) for x in input().split()]
enter.append(int(input()))

if dp(enter, len(enter)):
    print("Yes")
else:
    print("No")
