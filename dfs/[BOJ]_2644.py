from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline()

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited, count):
    visited[v] = 1
    
    if v == p2:
        return count        # 주의! 재귀함수에서는 return을 사용하더라도 바로 직전에 호출된 dfs 함수로만 전달되고 최종적으로는 전달되지 않는다

    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            result = dfs(graph, i, visited, count)
            if result != -1:    # 탐색 성공 여부를 확인하는 변수를 두어 목표 노드가 발견되면 result는 count 값을 반환할 수 ㅣㅇㅆ음.
                return result
        
    
    return -1
            
    
print(dfs(graph, p1, visited, 0))
