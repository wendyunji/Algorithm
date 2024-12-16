t = int(input())

d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4,12):
    d[i] = d[i-1] + d[i-2] + d[i-3]

result = []

for _ in range(t):
    n = int(input())
    result.append(d[n])

for r in result:
    print(r)
