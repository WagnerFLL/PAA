import sys

sys.setrecursionlimit(9999999)
memo = {}


def dp(adega, year, begin, end):
    if (end == begin):
        return year * adega[end]

    if ((begin, end, year) in memo):
        return memo[begin, end, year]

    a = dp(adega, year + 1, begin + 1, end) + adega[begin] * year
    b = dp(adega, year + 1, begin, end - 1) + adega[end] * year

    if (a > b):
        memo[begin, end, year] = a
        return a
    memo[begin, end, year] = b
    return b


n = int(input())
adega = []

for i in range(n):
    adega.append(int(input()))

print(dp(adega, 1, 0, n - 1))