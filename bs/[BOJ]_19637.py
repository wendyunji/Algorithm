import sys
input = sys.stdin.readline

n, m = map(int, input().split())

names = []
levels = []
scores = []

for _ in range(n):
    name, level = input().split()
    names.append(name)
    levels.append(int(level))

for _ in range(m):
    scores.append(int(input()))

def bs(array, target, start, end):

    while start <= end:
        mid = (start+end) // 2

        # 이것도 levels라는 배열에서 최솟값 찾기
        if array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return start

for score in scores:
    print(names[bs(levels, score, 0, n-1)])