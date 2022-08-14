import copy


def rotated(key):
    n = len(key)
    m = len(key[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
    return result


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] += lock[i][j]

    for _ in range(4):
        key = rotated(key)
        for x in range(n * 2):
            for y in range(n * 2):
                temp_lock = copy.deepcopy(new_lock)
                for i in range(m):
                    for j in range(m):
                        temp_lock[x + i][y + j] += key[i][j]

                answer = True
                for i in range(n, n * 2):
                    for j in range(n, n * 2):
                        if temp_lock[i][j] != 1:
                            answer = False
                if answer == True:
                    return answer

    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
