m = 1

while True:
    n = int(input())
    if n == 0:
        break

    nameFriends = input().split()

    friends = {}
    dependence = {}
    for x in range(n):
        friends[nameFriends[x]] = []

    for x in range(n):
        enter = input().split()
        dependence[enter[0]] = int(enter[1])
        for i in range(int(enter[1])):
            friends[enter[i + 2]].append(enter[0])

    q = []
    p = []
    a = 0

    for name in nameFriends:
        if dependence[name] == 0:
            q.append(name)
            a += 1

    while a > 0:
        node = q.pop(0)
        p.append(node)
        a -= 1
        for cp in friends[node]:
            dependence[cp] -= 1
            if dependence[cp] == 0:
                q.append(cp)
                a += 1

    print("Teste " + str(m))
    if (len(p) == n):
        print(*p)
    else:
        print("impossivel")
    print()
    m += 1