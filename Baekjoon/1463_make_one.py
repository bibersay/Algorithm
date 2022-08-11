from collections import deque

N = int(input())

dp = [0] * (N + 1)
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])

print(dp[N])



def BFS(start, cnt):
    queue.append((start, cnt))

    while queue:
        x, i = queue.popleft()
        if x == 1:
            print(i)
            break
        queue.append((x - 1, i + 1))
        if x % 3 == 0:
            queue.append((x / 3, i + 1))
        if x % 2 == 0:
            queue.append((x / 2, i + 1))

BFS(N,0)