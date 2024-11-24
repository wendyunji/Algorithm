import sys
sys.setrecursionlimit(10**6)

n, e, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
order = 1

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 내림차순 정렬
for i in range(n+1):
    graph[i].sort(reverse=True)

def dfs(graph, v, visited):
    global order
    visited[v] = order
    order += 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

dfs(graph, r, visited)

visited.pop(0)

for i in visited:
    print(i)