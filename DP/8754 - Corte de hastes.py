while True:

    n = int(input())
    if n == 0:
        break

    table = []
    for x in range(n):
        m = int(input())
        table.append(m)

    value = [0] * (n + 1)

    for i in range(1, n + 1):
        maximum = -10000
        for j in range(i):
            maximum = maximum if maximum > table[j] + value[i - j - 1] else table[j] + value[i - j - 1]
        value[i] = maximum

    print(value[n])