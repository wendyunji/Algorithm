n = int(input())
if n == 1:
	print(1)
else:
	dp = [0] * n
	dp[0] = 1 
	dp[1] = 1
	for i in range(2, n):
		dp[i] = dp[i - 2] + dp[i - 1] # '101'로 시작하는 경우 + '100'로 시작하는 경우
	print(dp[n - 1])