# 입력
n = int(input())
array = list(map(int, input().split()))

# DP 테이블 초기화 (각 위치에서의 LIS 길이)
dp = [1] * n

# LIS 계산
for i in range(n):
    for j in range(i):
        if array[j] < array[i]:  # 이전 원소가 현재 원소보다 작다면
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)

# 결과 출력
print(max(dp))  # LIS의 최대 길이
