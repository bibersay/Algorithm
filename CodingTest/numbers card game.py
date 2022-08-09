def solution(condition, numbers):
    result = 0
    n, m = condition
    minimum =[]
    for num in numbers:
        minimum.append((min(num)))

    result = max(minimum)
    return result


condition = [3,3]
numbers = [[3,1,2],[4,1,4],[2,2,2]]
print(solution(condition, numbers))
