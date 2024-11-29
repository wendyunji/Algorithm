from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
parents = [0 for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                parents[i] = v
                queue.append(i)
                visited[i] = 1

bfs(graph, 1, visited)

parents.pop(0)
parents.pop(0)

for parent in parents:
    print(parent)