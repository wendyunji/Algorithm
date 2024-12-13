n, m = map(int, input().split())

array = list(map(int, input().split()))

start = max(array)
end = sum(array)

def check(mid):
    blues = [0]
    i = 0
    # mid가 될 때까지 더해서 담아두기
    for a in array:
        if (blues[i] + a) > mid:
            i += 1  
            if i >= m:
                return False            
              
            blues.append(0)

        blues[i] += a

    return blues

result = []

while start <= end:
    mid = (start + end) // 2
    blues = check(mid)

    if blues:
        result = blues
        end = mid - 1
        
    else:
        start = mid + 1

print(max(result))

        