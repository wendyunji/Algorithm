t = int(input())

results = []

for _ in range(t):

    a, b = map(int, input().split())

    cnt1 = 1
    for i in range(b-a+1,b+1):
        cnt1 *= i

    cnt = 1
    for i in range(1,a+1):
        cnt *= i

    results.append(int(cnt1/cnt))

for result in results:
    print(result)