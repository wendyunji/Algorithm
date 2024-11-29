import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m  = map(int, input().split())

graph =[[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

count = 0
for i in range(1, n+1):

    if visited[i] == 0:
        count += 1
        dfs(graph, i, visited)

print(count)