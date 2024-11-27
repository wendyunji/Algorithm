from collections import deque
import sys
sys.setrecursionlimit(10**6)
# ! 여기서 input = sys.stdin.readline 하면 value error 남!! 조심할것!
n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx, dy = [1,-1,0,0], [0,0,1,-1]

def bfs(x,y):
    queue = deque([(x,y)])

    while queue:
        # 큐에서 빼기
        x, y = queue.popleft()
        # 4방으로 살펴보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵의 범위를 넘어가는 경우
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue

            # 벽인 경우
            if graph[nx][ny] == 0:
                continue

            # 노드를 처음 방문하는 경우에 거리 증가
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    return graph[n-1][m-1]

print(bfs(0,0))