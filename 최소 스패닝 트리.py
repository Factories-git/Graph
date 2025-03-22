import sys
sys.setrecursionlimit(10**5)


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


edges = []
re = 0

v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))
edges.sort()

for w, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        re += w
print(re)