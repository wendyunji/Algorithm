import sys

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())

cost = 0
basket = []
result = 0

def div(array, m):
    global result
    left_cost = 0
    n = len(array)
    avg = m // n

    left = []
    for a in array:
        if a <= avg:
            left_cost += a
            basket.append(a)
        else:
            left.append(a)
    m = m - left_cost

    cnt = 0
    for b in left:
        if b > avg:
            cnt += 1
    if cnt == len(left):
        result = avg

    return left, basket, left_cost, m

if sum(array) <= m:
    result = max(array)
else:
    while cost <= m:
        array, basket, left_cost, m = div(array, m)
        cost += left_cost
        if left_cost == 0:
            break


print(result)
