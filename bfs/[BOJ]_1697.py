import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
graph = [-1 for _ in range(100000)]


def bfs(x):
    queue = deque([x])
    graph[x] = 0

    while queue:
        x = queue.popleft()
        moves = [x+1, x-1, 2*x]
        
        for move in moves:
            nx = move

            # 제외 조건
            if nx > 100000 or nx < 0:
                continue
            
            # 최단 기록이 기록되어있지 않으면 기록
            if graph[nx] == -1:
                queue.append(nx)
                graph[nx] = graph[x] + 1

            if nx == k:
                return graph[nx]

print(bfs(n))
