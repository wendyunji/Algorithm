t = int(input())

result =[]

for _ in range(t):
    n = int(input())
    d = [0]*(n+10)
    d[1] = 1
    d[2] = 1
    d[3] = 1
    d[4] = 2
    d[5] = 2
    d[6] = 3
    for i in range(7,n+1):
        d[i] = d[i-2] + d[i-3]

    result.append(d[n])

for a in result:
    print(a)