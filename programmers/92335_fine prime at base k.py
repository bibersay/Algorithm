def make_base_k(n, k):
    num = ''
    while n:
        d = n % k
        n //= k
        num += str(d)

    return num[::-1]


def find_prime(numbers):
    cnt = 0
    for num in numbers:
        if num == '':
            continue
        num = int(num)
        if num == 1:
            continue
        if num == 2 or num == 3:
            cnt += 1
            continue
        prime = True
        for i in range(3, int(num ** 0.5) + 1,2):
            if num % i == 0:
                prime = False
        if prime:
            cnt +=1
    return cnt


def solution(n, k):
    S = make_base_k(n, k)
    numbers = S.split('0')
    answer = find_prime(numbers)

    return answer


n = 437674
k = 3
print(solution(n, k))
