def solution(n):
    ans = 0

    while n:
        d = n % 2
        n //= 2
        ans += d

    return ans


n = 6
print(solution(n))
