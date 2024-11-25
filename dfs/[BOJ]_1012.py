# 이코테 음료수 얼려먹기와 흡사함
t = int(input())

def dfs(x, y):
    if x > n or y > m or x < 0 or y < 0:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    
    return False

results = []
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    result = 0

    for i in range(m):
        for j in range(n):
            if dfs(i,j) == 1:
                result += 1

    results.append(result)

for result in results:
    print(result)
