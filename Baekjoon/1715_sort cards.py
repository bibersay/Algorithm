import heapq
import sys

n = int(input())
queue = [int(sys.stdin.readline()) for _ in range(n)]

heapq.heapify(queue)
if n == 1:
    print(0)
else:

    result = 0
    while len(queue) >1:
        s = heapq.heappop(queue) + heapq.heappop(queue)
        result += s
        heapq.heappush(queue,s)
    print(result)