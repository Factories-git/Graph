import sys

input = sys.stdin.readline


def find_parent(parent, v):
    if parent[v] != v:
        parent[v] = find_parent(parent, parent[v])
    return parent[v]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        print(i+1)
        exit(0)
    else:
        union(parent, a, b)
print(0)