import sys

sys.setrecursionlimit(10**6)


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(parent, a, b)
    if c == 1:
        k = find(parent, a)
        d = find(parent, b)
        if k == d:
            print('yes')
        else:
            print('no')
