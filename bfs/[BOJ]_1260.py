from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited_dfs = [0 for _ in range(n+1)]
visited_bfs = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

dfs(graph, v, visited_dfs)
print('')
bfs(graph, v, visited_bfs)