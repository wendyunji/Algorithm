import sys

t = int(input())

def bs(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0

for _ in range(t):
    n = int(input())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(input())
    targets = list(map(int, sys.stdin.readline().rstrip().split()))

    array.sort()

    for target in targets:
        print(bs(array, target, 0, n-1))