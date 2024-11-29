from collections import deque

m, n, k = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    sx,sy,ex,ey = map(int, input().split())
    # 어디에 저장?
    for i in range(sx, ex):
        for j in range(sy, ey):
            graph[i][j] = -1

dx, dy = [1,-1,0,0], [0,0,1,-1]

counts = []

def bfs(x,y):
    global count
    queue = deque([(x,y)])
    graph[y][x] = 1

    while queue:
        nx, ny = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= m or ny >= n or nx < 0 or ny < 0:
                continue

            # 벽일 경우
            if graph[ny][nx] == -1:
                continue
            
            # 방문 안한 경우
            if graph[ny][nx] == 0:
                queue.append((nx, ny))
                graph[ny][nx] = 1
                count += 1
                print(count)



for i in range(m):
    for j in range(n):
        print(i,j)
        count = 0
        bfs(i, j)
        print(graph)
        counts.append(count)

print(counts)
