import sys
from collections import deque

N, M, K, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)


def BFS(start):
    queue = deque([])
    answer = []
    if visit[start] == 1:
        return
    visit[start] = 1
    queue.append((start, 0))
    while queue:
        node, cost = queue.popleft()
        if cost == K:
            answer.append(node)
            continue
        for g in graph[node]:
            if visit[g] == 0 and cost+1 <=K:
                queue.append((g, cost + 1))
                visit[g] = 1

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        print(*answer)


BFS(start)
