import sys
sys.setrecursionlimit(10**6)

w, h = -1, -1

count = 0

def dfs(x,y):

    # 범위를 벗어나는 경우
    if x >= h or x < 0 or y >= w or y < 0:
        return False

    # 바다인경우
    if graph[x][y] == 0:
        return False

    # 방문하지 않은 땅인경우
    if graph[x][y] != 0:
        graph[x][y] = 0
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x+1,y+1)
        dfs(x+1,y-1)
        dfs(x-1,y+1)
        dfs(x-1,y-1)
        return True
    
    return False

counts =[]

while w != 0 and h != 0:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                count += 1

    counts.append(count)
    count = 0


for count in counts:
    print(count)

