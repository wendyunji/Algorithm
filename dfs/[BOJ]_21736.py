import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))

sx, sy = 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            sx, sy = i, j
            break

# way 1 그래프만 써서 P를 마주치면 숫자 올리기
# way 2 visited를 만들어서 P가 몇개인지 보기

dx, dy = [0,0,1,-1], [1,-1,0,0]

count = 0

def dfs(x,y):
    global count    

    # 맵 조건을 벗어나는 경우
    if x >= n or y >= m or x < 0 or y < 0:
        return False

    # 벽인 경우
    if graph[x][y] == 'X':
        return False

    # 처음 방문하는 경우
    if graph[x][y] != 1:
        
        if graph[x][y] == 'P':
            count += 1

        graph[x][y] = 1
        
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        
        return True

dfs(sx, sy)

if count == 0:
    print('TT')
else:
    print(count)