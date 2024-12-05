import sys

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()

def bs(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            return 1
        
        elif target < array[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return 0

for target in targets:
    print(bs(array, target, 0, n-1))