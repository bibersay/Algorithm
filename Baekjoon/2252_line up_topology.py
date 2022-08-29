import sys
from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    indegree[b] += 1
    graph[a].append(b)

queue = deque()
for j in range(1, len(indegree)):
    if indegree[j] ==0 :
        queue.append(j)
answer = []
while queue:
    now = queue.popleft()
    answer.append(now)
    for g in graph[now]:
        indegree[g] -=1
        if indegree[g] == 0:
            queue.append(g)

print(*answer)
