import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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
    # 범위에서 벗어날 경우
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    
    # 벽일 경우 (= 기준점보다 낮거나 같을 경우)
    if graph[x][y] <= l:
        return False

    if graph[x][y] > l:
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny,l)
            
        return True
        
    return False

safes = []



for l in range(high):
    safe = 0
    graph = copy.deepcopy(resetg)

    for i in range(n):
        for j in range(n):
            if dfs(i,j,l) == True:
                safe += 1

    safes.append(safe)

print(max(safes))
    

