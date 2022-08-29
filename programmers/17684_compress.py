def solution(msg):
    answer = []
    S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = {}
    for i, s in enumerate(S):
        index[s] = i + 1

    w, c = 0,0

    while True:
        c +=1
        if c == len(msg):
            answer.append(index[msg[w:c]])
            break
        if msg[w:c+1] not in index:
            index[msg[w:c+1]] = len(index)+1
            answer.append(index[msg[w:c]])
            w = c

    return answer


msg = 'KAKAO'
print(solution(msg))
