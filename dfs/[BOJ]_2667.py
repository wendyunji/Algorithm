n = int(input())

mp = [[] for _ in range(n)]

for i in range(n):
    a = input()
    for j in range(n):
        mp[i].append(int(a[j]))

print(mp)

visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(mp, x, y, visited):
    if mp[x][y] == 0:
        visited[x][y] = -1
    else:
        visited[x][y] = 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx > 0 and ny > 0 and nx < n and ny < n:
            if mp[nx][ny] == 0:
                visited[x][y] = -1
            else:
                visited[x][y] = 1
                if visited[nx][ny] == 0:
                    dfs(mp, nx, ny, visited)

dfs(mp, 0, 0, visited)

print(visited)

    



# def dfs(graph, v, visited):
#     visited[v] = 1

#     for i in graph[v]:
#         if visited[i] == 0:
#             dfs(graph, i, visited)