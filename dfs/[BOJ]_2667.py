import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

counts = []
count = 0
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

test = [0]

def dfs(x,y):
    global count
    if x >= n or y >= n or x < 0 or y < 0:
        return False

    if graph[x][y] == '1':
        count += 1
        # test[result] += 1
        graph[x][y] = '0'

        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)

        return True

    return False

dx, dy = [1,-1,0,0], [0,0,1,-1]

result = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            # test.append(0)
            counts.append(count)
            count = 0
            # result += 1

print(len(counts))
for count in counts:
    print(count)

# print(result)

# test.pop()
# test.sort()

# for t in test:
#     print(t)
