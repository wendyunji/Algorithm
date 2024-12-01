import sys

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()

def bs(array, target, start, end):
    global count

    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            del array[mid]
            count += 1
            return True
        
        elif target < array[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return False

for target in targets:
    result = True
    count = 0
    while result == True:
        result = bs(array, target, 0, len(array)-1)
    print(count, end=' ')