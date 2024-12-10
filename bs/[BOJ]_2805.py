n, m = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    tree = 0
    mid = (start + end) // 2

    for a in array:
        if a >= mid:
            tree += a - mid
        else:
            tree += 0

    if tree >= m:
        start = mid + 1
    else:
        end = mid - 1
        

print(end)