n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
graph2 = set()
for i in range(m):
    ipt = (graph[i][0], graph[i][1])
    if graph[i][0] < graph[i][1]:
        ipt = (graph[i][1], graph[i][0])
    if graph[i][0] == graph[i][1]:
        continue
    graph2.add(ipt)
print(m - len(graph2))