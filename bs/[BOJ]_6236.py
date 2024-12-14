n, m = map(int, input().split())

array = []

for _ in range(n):
    array.append(int(input()))

start = max(array)
end = sum(array)

cost = [0]

def check(mid):
    global cost
    result = 0
    cnt = 0
    results = [0]
    for a in array:

        if (result+a) <= mid:
            result += a
        else:
            cnt += 1
            cost = results
            if cnt >= m:
                return False
            result = a
            results.append(a)
        results[cnt] = result

    cost = results

    return results            



while start <= end:
    mid = (start+end) // 2

    results = check(mid)
    # print(results, mid)
    if results:
        end = mid - 1
        
    else:
        start = mid + 1

# print(cost)
print(max(cost))
# print(start)

