import sys
import copy
sys.setrecursionlimit(10**6)

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

resetg = copy.deepcopy(graph)

high = 0
# 최대 높이 찾기
for i in range(n):
    if max(graph[i]) > high:
        high = max(graph[i])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,l):
    graph[x][y] = -1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위에서 벗어날 경우
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        
        # 벽일 경우 (= 기준점보다 낮거나 같을 경우)
        if graph[nx][ny] <= l:
            continue

        # 안전영역이면서 방문하지 않았을 경우 (방문 안하면 무조건 -l은 아님)
        if graph[nx][ny] > l:
            dfs(nx, ny,l)
            graph[nx][ny] = -1
            return True
        
        return False

safes = []

for l in range(high):
    safe = 0
    print(l)
    graph = copy.deepcopy(resetg)
    print(graph)
    for i in range(n):
        for j in range(n):
            # print(i,j,l)
            if dfs(i,j,l) == True:
                safe += 1
    safes.append(safe)
    print(safes)
    

