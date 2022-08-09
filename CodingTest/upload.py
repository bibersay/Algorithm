def solution(order):
    answer = 0
    temp = []

    next = order[0]
    if next >= 2:
        for k in range(next - 1):
            temp.append(k + 1)

    answer += 1
    i = 1
    while i < len(order):
        if order[i] == next + 1:
            answer += 1
            next = order[i]
        elif len(temp) > 0 and temp[-1] == order[i]:
            next = order[i]
            temp.pop()
            answer += 1
        elif next +1 < order[i]:
            for j in range(next - 1, order[i] - 1):
                temp.append(j + 1)
            answer += 1
            next = order[i]
        else:
            break
        i += 1
    return answer


order = [5, 4, 3, 2, 1]
print(solution(order))
