import bisect


def solution(words, queries):
    answer = []
    reverse_word = [[] for _ in range(10001)]
    word = [[] for _ in range(10001)]
    for w in words:
        reverse_word[len(w)].append(w[::-1])
        word[len(w)].append(w)
    for i in range(10001):
        word[i].sort()
        reverse_word[i].sort()

    for q in queries:
        if q[0] == "?":
            reverse_q = q[::-1]
            left_index = bisect.bisect_left(reverse_word[len(reverse_q)], reverse_q.replace('?', 'a'))
            right_index = bisect.bisect_right(reverse_word[len(reverse_q)], reverse_q.replace('?', 'z'))
        else:
            left_index = bisect.bisect_left(word[len(q)], q.replace('?', 'a'))
            right_index = bisect.bisect_right(word[len(q)], q.replace('?', 'z'))
        answer.append(right_index - left_index)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
