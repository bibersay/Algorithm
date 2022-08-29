n = int(input())
finish = [[] for _ in range(n + 1)]
t = []
p = []
for _ in range(n):
    T, bonus = map(int, input().split())
    t.append(T)
    p.append(bonus)

dp = [0] * (n + 2)

#첫날부터 계산
# for i in range(1,n+1):
#     time = t[i-1] + i-1
#     dp[i] = max(dp[i] , dp[i-1])
#     if time <= n:
#         dp[time] = max(dp[time], dp[i-1]+p[i-1])

for i in range(n-1,-1,-1):
    time = t[i] + i
    if time <=n:
        dp[i] = max(dp[time]+ p[i], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(max(dp))
