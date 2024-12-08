n = int(input())
m = int(input())

array = list(map(int, input().split()))

def check(array, mid):
    if ( (array[0] - mid) <= 0 ) and ( (array[-1] + mid) >= n ):
        for i in range(len(array)-1):
            if (array[i] + mid) < (array[i+1] - mid):
                return False
        return True

    else:
        return False


# 조건을 만족하는 최소 n 값 찾기
def bs(array,start, end):

    while start <= end:

        mid = (start + end) // 2

        # array에 있는 원소들의 조건 확인
        if check(array, mid) == True:
            end = mid - 1
        else:
            start = mid + 1
            
    return start

print(bs(array, 0, n))