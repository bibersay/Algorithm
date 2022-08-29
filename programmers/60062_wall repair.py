from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    combinations = list(permutations(dist, len(dist)))
    answer = len(dist) + 1
    for start in range(length):
        for combination in combinations:
                cnt = 1
                position = weak[start] + combination[cnt-1]
                for i in range(start, start + length):
                    if position < weak[i]:
                        cnt += 1
                        if cnt > len(combination):
                            break
                        position = weak[i] + combination[cnt - 1]
                answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n, weak, dist))
