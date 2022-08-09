def solution(want, number, discount):
    answer = 0
    window = [0] * len(want)
    equal = False
    if len(discount) < len(want):
        return 0

    for i, item in enumerate(discount):
        if item in want:
            window[want.index(discount[i])] += 1
        if i >= 10 and discount[i - 10] in want and window[want.index(discount[i - 10])] > 0:
            window[want.index(discount[i - 10])] -= 1
        # print(sum(window))
        for k in range(len(window)):
            if window[k] >= number[k]:
                equal = True
            else:
                equal = False
                break
        if equal:
           answer += 1


    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana",
            "apple", "banana"]
print(solution(want, number, discount))
