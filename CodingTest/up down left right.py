def solution(direction):
    result = [1, 1]
    N = 5
    for d in direction:
        if d == 'R':
            dx = 1
            dy = 0
        if d == 'L':
            dx = -1
            dy = 0
        if d == 'U':
            dx = 0
            dy = -1
        if d == 'D':
            dx = 0
            dy = 1
        if 1 <= result[1] + dx <= N and 1 <= result[0] + dy <= N:
            result[1] += dx
            result[0] += dy

    return result


direction = ["R", "R", "R", "U", "D", "D"]
print(solution(direction))
