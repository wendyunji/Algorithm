import sys

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()

array_dict = {}

for i in array:
    if i in array_dict:
        array_dict[i] += 1
    else:
        array_dict[i] = 1

def bs(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            return array_dict[target]
        
        elif target < array[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return 0

for target in targets:
    print(bs(array, target, 0, len(array)-1), end=' ')