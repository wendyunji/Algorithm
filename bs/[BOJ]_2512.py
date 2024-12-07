import sys

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())

start = 1
end = max(array)

while start <= end:
    mid = (start+end) // 2
    cost = 0
    for a in array:
        if a > mid:
            cost += mid
        else:
            cost += a
    if cost <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)


   