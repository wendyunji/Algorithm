import sys
input = sys.stdin.readline

n, k = map(int, input().split())

array = []

for _ in range(n):
    array.append(int(input()))


start = 0
end = max(array)

while start <= end:
    mid = (start+end) // 2
    result = 0

    if sum(array) < k:
        end = 0 
        break

    if mid == 0:
        mid = 1

    for a in array:
        if a >= mid:
            result += (a // mid)

    if result >= k:
        start = mid + 1
    else:
        end = mid -1

print(end)