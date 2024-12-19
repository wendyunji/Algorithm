
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [[0] * 15 for _ in range(15)]

    for i in range(1, 15):
        dp[0][i] = i

    for i in range(1, 15):
        dp[i][1] = 1

    for x in range(1, 15):
        for y in range(2, 15):
            dp[x][y] = dp[x][y-1] + dp[x-1][y]

    # 5. 원하는 형식으로 출력
    print(dp[k][n])