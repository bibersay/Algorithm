N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * i for i in range(1, N + 1)]
for i, tri in enumerate(triangle):
    if i == 0:
        dp[0][0] = triangle[0][0]
        continue
    elif i == 1:
        dp[1][0] = dp[0][0] + triangle[1][0]
        dp[1][1] = dp[0][0] + triangle[1][1]
        continue
    for j, t in enumerate(tri):
        if j == 0:
            dp[i][0] = dp[i-1][0] + t
        elif 1 <= j < i:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + t
        elif i == j :
            dp[i][j] = dp[i-1][j-1] + t


print(max(dp[-1]))
