import sys
input = sys.stdin.readline

m, n = map(int, input().split())

array = list(map(int, input().split()))

result = 0      # 과자를 먹을 수 있는 사람의 명수
start = 0
end = max(array)

while start <= end:
    mid = (start+end) // 2
    result = 0

    if sum(array) < m:
        end = 0
        break

    if mid == 0:
        mid = 1

    # 과자 길이 계산하기
    for a in array:
        if (a // mid) >= 1:
            result += (a//mid)

    if result >= m:
        start = mid + 1
    else:
        end = mid -1

print(end)