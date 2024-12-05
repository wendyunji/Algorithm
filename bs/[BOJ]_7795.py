import sys

t = int(input())

def bs(array, target, start, end):
    a = 0
    while start <= end:
        mid = (start+end) // 2

        if array[mid] <=  target:
            start = mid + 1
        
        else:
            end = mid - 1
    
    return start

sums = []

for _ in range(t):
    a, b = map(int, input().split())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    targets = list(map(int, sys.stdin.readline().rstrip().split()))

    array.sort()
    targets.sort()

    sum = 0

    for target in targets:
        a = bs(array, target, 0, (len(array)-1))
        
        if a == 0:
            sum += 0
        else:
            sum += (len(array)-a)

    sums.append(sum)

for sum in sums:
    print(sum)