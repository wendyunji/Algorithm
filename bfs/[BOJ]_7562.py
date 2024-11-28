from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

dx = [-2, -1, 2, 1, -2, -1, 2, 1]
dy = [1, 2, 1, 2, 1, 2, 1, 2]
counts = []
def bfs(x,y):
    global count
    global ex, ey
    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 벗어난 경우 제외
            if nx >= l or ny >= l or nx < 0 or ny < 0:
                continue


            # 최단 거리 기록이 없으면 기록
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[ey][ex]

for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    graph = [[0 for _ in range(l)] for _ in range(l)]
    counts.append(bfs(sx, sy))
    # print(graph)

for count in counts:
    print(count)