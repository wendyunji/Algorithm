n, m = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

start = 0
end = sum(array)

while start <= end:
    mid = (start + end) // 2
    blues = [0]

    i = 0
    # mid가 될 때까지 더해서 담아두기
    for a in array:
        if (blues[i] + a) >= mid:
            blues.append(0)
            i += 1    
        blues[i] += a

    if len(blues) == m:
        if mid*m <= sum(blues):
            start = mid + 1
        else:
            end = mid - 1
    elif len(blues) > m:
        start = mid + 1
    else:
        end = mid - 1

print(blues)
print(max(blues))
        