n = int(input())
dp = list(map(int, input().split()))

count = [1] * n
count[0] = 1
for i in range(1, n):
    for j in range(i):
        if dp[j] > dp[i]:
            count[i] = max(count[i], count[j] + 1)
print(n - max(count))
