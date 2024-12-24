n = int(input())

dp = [[0]]*n

for i in range(n):
    dp[i] = dp[i] + list(map(int, input().split())) + [0,0,0,0]

for i in range(1,n):
    for j in range(1,len(dp[i])-3):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]

print(max(dp[-1]))
    