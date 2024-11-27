from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
order = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort(reverse=True)

def bfs(graph, start, visited):
    global order
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        order += 1
        visited[v] = order
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


bfs(graph, r, visited)

visited.pop(0)

for order in visited:
    print(order)