import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

results = []

def dfs(y,x):
    # index error
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    
    # 현위치가 1 이라면 그 주변을 탐색하면서 1을 0으로 바꿔서 연결된 부분을 모두 0으로 바꾸고 True 반환하기
    # 즉 위치를 하나씩 탐색하면서 0 칠하기
    if graph[y][x] == 1:
        graph[y][x] = 0

        dfs(y+1, x)  # 아래
        dfs(y-1, x)  # 위
        dfs(y, x+1)  # 오른쪽
        dfs(y, x-1)  # 왼쪽
        return True

    return False


for _ in range(t):
    m, n, k, = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    # 그래프 입력 받기
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1


    result = 0
    
    # 탐색 시작
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    results.append(result)

for result in results:
    print(result)