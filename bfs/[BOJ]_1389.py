from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1
    
    return visited

bacons = []

for i in range(1,n+1):
    bacon = bfs(graph, i, visited)

    bacons.append(sum(bacon) + 1)

    visited = [-1 for _ in range(n+1)]

minimum = bacons[0]
idx = 1

for i in range(len(bacons)):
    if bacons[i] < minimum:
        minimum = bacons[i]
        idx = i+1

print(idx)