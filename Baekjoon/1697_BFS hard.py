from collections import deque
import sys

sys.setrecursionlimit(10 * 6)

N, M = map(int, input().split())
queue = deque()
point = [0] * 100001


def BFS(start):
    queue.append(start)

    while queue:
        pre = queue.popleft()
        if pre == M:
            return point[pre]
        for present in [pre - 1, pre + 1, pre * 2]:
            if 0 <= present <= 10 ** 5 and not point[present]:
                point[present] = point[pre] + 1
                queue.append(present)


print(BFS(N))
