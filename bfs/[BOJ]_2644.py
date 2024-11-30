from collections import deque
import sys
sys.setrecursionlimit(10**6)
# input = sys.stdin.readline()

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start, visited):
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v]+1
                if i == p2:
                    return visited[i]
                
    return -1


print(bfs(graph, p1, visited))
