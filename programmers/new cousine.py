from itertools import combinations


def courses(orders, course):
    menu = []
    for c in course:
        temp = []
        for order in orders:
            temp += list(combinations(order, c))
        menu.append(list(set([''.join(sorted(t)) for t in temp])))
    return menu


def solution(orders, course):
    combinations = courses(orders, course)
    candidates = {}
    for comb in combinations:
        if comb:
            candidates[len(comb[0])] = comb

    count = {}
    for num, candidate in candidates.items():  # combinations of each course size
        for S in candidate:  # one combination of course of num size  ('A','C')
            cnt = 0
            for order in orders:  # check combination is in order
                S_is_in_order = True
                for s in S:  # 'A' is in order? after 'C' is in order?
                    if s not in order:
                        S_is_in_order = False
                if S_is_in_order:
                    cnt += 1
            if cnt >= 2:
                if len(S) not in count:
                    count[len(S)] = [(cnt, S)]
                else:
                    count[len(S)] += [(cnt, S)]
    #
    # print(count)
    answer = []
    for s in course:
        if s not in count :
            continue
        temp = list(count[s])
        temp.sort(reverse=True)
        max_temp = max(temp)
        rest_list = list(filter(lambda x: x[0] == max_temp[0], temp))
        for rest in rest_list:
            answer.append(rest[1])
        answer.sort()
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))
