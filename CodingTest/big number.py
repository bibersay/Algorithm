def solution(condition, numbers):
    result = 0
    n, m, k = condition
    max_number = max(numbers)
    numbers.pop(numbers.index(max_number))
    max_2_number = max(numbers)
    result = max_number

    for i in range(1, m):
        if i % k + 1 == k:
            result += max_2_number
        if i % k + 1 != k:
            result += max_number

    return result


condition = [5, 8, 3]
numbers = [2, 4, 5, 4, 6]
print(solution(condition, numbers))
