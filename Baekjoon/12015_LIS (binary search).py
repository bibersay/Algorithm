import sys

n = int(input())
S = list(map(int, sys.stdin.readline().split()))


def N_square():
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if S[i] > S[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    print(max(dp), dp.index(max(dp)), dp)


def N_logN():
    dp = [0]

    for i in range(n):
        if S[i] <= dp[-1]:
            start = 0
            end = len(dp)-1
            while start < end:
                mid = (start + end) // 2
                if dp[mid] < S[i]:
                    start = mid + 1
                elif dp[mid] > S[i]:
                    end = mid
                else:
                    end = start = mid
            dp[end] = S[i]
        else:
            dp.append(S[i])
    print(len(dp) - 1)


N_square()
N_logN()
