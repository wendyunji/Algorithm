n = int(input())
e = int(input())

graph = [[] for _ in range(n+1)]

for i in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]

def dfs(graph, v, visited):
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

cnt = 0

for i in visited:
    if i == 1:
        cnt += 1
        
# 찾아보니 이거 말고 그냥 sum(visited 해도 됨)
# print(sum(visited)-1)

print(cnt-1)