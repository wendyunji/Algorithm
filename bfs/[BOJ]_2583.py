from collections import deque

m, n, k = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    sx,sy,ex,ey = map(int, input().split())
    # 어디에 저장?
    for i in range(sx, ex):
        for j in range(sy, ey):
            graph[i][j] = 1

dx, dy = [1,-1,0,0], [0,0,1,-1]

counts = []

def bfs(x,y):
    global count
    queue = deque([(x,y)])
    graph[x][y] = 1

    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue

            # 벽일 경우
            if graph[nx][ny] == -1:
                continue
            
            # 방문 안한 경우
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1
                count += 1
    

count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            count = 1
            bfs(i, j)
            counts.append(count)
            
counts.sort()

print(len(counts))

for count in counts:
    print(count)
