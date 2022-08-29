def solution(dots, lines):
    if len(dots) == 1:
        return 1

    answer = 1
    sub_sum = []
    sum_sum = [0]

    for i in range(len(dots) - 1):
        sub_sum.append(dots[i + 1] - dots[i])
        sum_sum.append(sub_sum[i]+dots[i])
    print(sub_sum)
    print(sum_sum)
    length = 0
    line_index = len(lines) - 1
    sub_sum_index = 0

    while sub_sum_index < len(sub_sum):
        length += sub_sum[sub_sum_index]
        if lines[line_index] < length:
            line_index -= 1
            if line_index < 0:
                return -1
            sub_sum_index += 1
            answer += 1
            length = sub_sum[sub_sum_index]
        sub_sum_index += 1
        print(f'{sub_sum=} {lines=} {sub_sum_index=} {length=} {line_index=} {answer=}')

    return answer


dots = [1, 3, 4, 6, 7, 10]
lines = [2, 2, 2, 2]
print(solution(dots, lines))
