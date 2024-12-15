n = int(input())
f,s = map(int, input().split())
graph = [[] for _ in range(n+1)]
l = list(map(int, input().split()))
for i in range(1,n+1):
    graph[i].append(l[i-1])
print(graph)