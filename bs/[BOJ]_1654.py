k, n = map(int, input().split())

lans = []

for _ in range(k):
    lans.append(int(input()))

start = 1
end = max(lans)
result = 0

while start <= end:
    result = 0
    mid = (start+end) // 2

    for lan in lans:
        result += (lan // mid)

    if result >= n:
        start = mid + 1
        
    else:
        end = mid - 1


print(end)

