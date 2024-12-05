import sys

t = int(input())

def bs(array, target, start, end):
    a = 0
    while start <= end:
        mid = (start+end) // 2

        if array[mid] >  target:
            a = mid
            end = mid - 1
        # start와 end가 같아질때까지 찾아내기
        else:
            start = mid + 1
    
    return a

sums = []

for _ in range(t):
    a, b = map(int, input().split())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    targets = list(map(int, sys.stdin.readline().rstrip().split()))

    array.sort()

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