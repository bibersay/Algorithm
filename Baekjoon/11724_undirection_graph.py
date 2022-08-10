from collections import deque
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[] for _ in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
visit = [0] * V

def DFS(start):
    visit[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.pop()
        for g in graph[x]:
            if not visit[g]:
                visit[g] =1
                queue.append(g)

def BFS(start):
    queue = deque()
    queue.append(start)
    visit[start] = 1
    while queue:
        x = queue.popleft()
        for g in graph[x]:
            if not visit[g]:
                visit[g] = 1
                queue.append(g)

cnt = 0
for i in range(V):
    if not visit[i]:
        DFS(i)
        cnt += 1



print(cnt)
