n = int(input())

array = list(map(int, input().split()))

d =[[array[0]]]

for a in range(1, len(array)):
    b = array[a]
    k = len(d)
    for i in d:
        if i[-1] < b:
            i.append(b)
    if len(d) <= k:
        d.append([b])

m = 0

for i in d:
    if len(i) > m:
        m = len(i)

print(m)        

