import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2)
        answer+=1
    if scoville[0] <K:
        return -1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    scoville_now = heapq.heappop(scoville)
    while scoville_now < K:
        if len(scoville) < 1:
            return -1
        scoville_now += heapq.heappop(scoville) * 2
        heapq.heappush(scoville, scoville_now)
        # heapq.heapify(scoville)
        scoville_now = heapq.heappop(scoville)
        cnt += 1

    return cnt