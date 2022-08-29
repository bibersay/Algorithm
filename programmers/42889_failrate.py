
"""
stage 오름차순
set, list 오름차순
min 값과 min의 count -> fail rate = count / N
stage list.append(fail rate)
set 에서 min 제거후 반복
min 값과 min의 count -> fail rate = count / n - prev_count
fail list에서 내림차순 정렬 출력
"""

from collections import Counter

def solution(N, stages):
    answer = []
    count = Counter(stages)

    n = len(stages)
    fail_rate = []
    for i in range(1,N+1):
        if i in count:
            cnt = count[i]
        else:
            fail_rate.append((0,i))
            continue
        fail_rate.append((cnt/n,i))
        n -= cnt
    fail_rate.sort(key=lambda x: x[0], reverse=True)
    for i in range(len(fail_rate)):
        answer.append(fail_rate[i][1])

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
