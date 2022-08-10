N = int(input())
color = [list(map(int, input().split())) for _ in range(N)]


dp = [[1000] * 3 for _ in range(N)]
dp[0] = color[0]
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + color[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + color[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + color[i][2]
print(min(dp[-1][0], dp[-1][1], dp[-1][2]))

while True:
    pass