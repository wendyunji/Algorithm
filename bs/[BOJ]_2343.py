n, m = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

start = max(array)
end = sum(array)

def check(mid):
    
    i = 0
    # mid가 될 때까지 더해서 담아두기
    for a in array:
        if (blues[i] + a) >= mid:
            blues.append(0)
            i += 1    
            if i >= m:
                return False
        blues[i] += a

    return True


while start <= end:
    mid = (start + end) // 2
    blues = [0]

    if check(mid) == True:
        end = mid - 1
    else:
        start = mid + 1


print(end)

        