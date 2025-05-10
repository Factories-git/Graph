import sys
sys.setrecursionlimit(10**5)


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
re = []
n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

for w, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        re.append(w)
print(sum(re) - max(re))