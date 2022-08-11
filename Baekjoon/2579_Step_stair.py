step = [int(input()) for _ in range(int(input()))]
print(step)

dp = [0] * len(step)
dp[0] = step[0]
dp[1] = dp[0] + step[1]
dp[2] = max(dp[0], dp[1]) + step[2]
for i in range(3, len(step)):
    dp[i] = max(dp[i - 3] + step[i - 1], dp[i - 2]) + step[i]

print(dp[-1])
