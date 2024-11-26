from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph=[[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
orders = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def bfs(graph, start, visited):
    # 초기 설정
    visited[start] = 1
    order = 0
    queue = deque([start])
    # 반복
    while queue:
        v = queue.popleft()     # 탐색 노드 빼기
        order += 1
        orders[v] = order
        for i in graph[v]:      # 탐색 노드의 이웃노드
            if visited[i] == 0: # 방문하지 않았다면
                queue.append(i) # 큐에 넣고
                visited[i] = 1  # 방문처리 하기

bfs(graph, r, visited)

orders.pop(0)    

for order in orders:
    print(order)