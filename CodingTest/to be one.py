def solution(numbers):
    result = 0
    num = numbers[0]
    k = numbers[1]
    while True:
        if num == 1:
            return result
        while num % k == 0:
            num /= k
            result +=1
        num -= 1
        result += 1

    return result


numbers = [25, 5]
print(solution(numbers))
