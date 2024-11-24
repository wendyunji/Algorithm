# 특이점 : 시작 정점이 따로 있음 & 방문 순서를 출력함 & 낮은 번호부터 탐색

n, e, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _  in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(e):
    graph[i].sort()

order = 1

def dfs(graph, v, visited):
    # 전역 변수를 함수 내에서 쓸때 이렇게 선언하는 것 유의할 것
    global order
    visited[v] = order
    order += 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

dfs(graph, r, visited)

for i in range(1, len(visited)):
    print(visited[i])