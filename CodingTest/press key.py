def select_hand(right, left, pos):
    if pos in [1, 4, 7]:
        h = "L"
        l_pos = pos
    elif pos in [3, 6, 9]:
        h = "R"
        r_pos = pos

    elif pos in [2, 5, 8, 10]:
        if left in [1, 4, 7]:
            l_dis = abs(pos - left - 1) // 3 + 1
        elif left in [2, 5, 8, 10]:
            l_dis = abs(pos - left - 1) // 3

        if right in [3, 6, 9]:
            r_dis = abs(right - 1 - pos) // 3 + 1
        elif left in [2, 5, 8, 10]:
            r_dis = abs(right - 1 - pos) // 3

        h = "R" if l_dis > r_dis else "L"
        if l_dis == r_dis:
            h = hand

    return h , r_pos, l_pos

    return hand


def solution(numbers, hand):
    answer = ''

    l_pos = '*'
    r_pos = '#'

    for i in numbers:
        h, r_pos, l_pos = select_hand(r_pos, l_pos, i)
        answer +=h

        print(answer)
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))
