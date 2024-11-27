from collections import deque

n, m = map(int, input().split())

graph = []
count = 0
for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(m):
        graph[i][j] = int(graph[i][j])

dx, dy = [1,-1,0,0], [0,0,1,-1]

def bfs(x,y):
    global count
    queue = deque([(x,y)])

    while queue:
        vx, vy = queue.popleft()
        if vx == m-1 and vy == n-1:
            return True
        
        if x>=0 or y>=0 or x<m or x<n:
            if graph[vx][vy] == 1:
                graph[vx][vy] = 0
                count += 1
                print(count)
                for i in range(4):
                    x = vx + dx[i]
                    y = vy + dy[i]
                    if x>=0 or y>=0 or x<m or x<n:
                        queue.append((x,y))

print(bfs(0,0))

# 1의 개수는 찾아냄