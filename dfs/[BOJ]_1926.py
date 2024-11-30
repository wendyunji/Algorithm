import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

count = 0
counts = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x,y):
    global count

    # 맵의 외부일 경우
    if x >= n or y >= m or x < 0 or y < 0:
        return False
    
    # 그림이 아닌 벽일 경우
    if graph[x][y] == 0:
        return False

    # 그림이 아직 안칠해질 경우
    if graph[x][y] == 1:
        graph[x][y] = 0     # 벽으로 매꿔줌
        
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)

        count += 1

        return True
    
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            counts.append(count)
            count = 0

print(len(counts))

if len(counts) == 0:
    print(0)
else:
    print(max(counts))