from collections import deque

N, K = map(int, input().split())
graph = []
temp = [[] for _ in range(K)]
for i in range(N):
    g = list(map(int, input().split()))
    for j in range(len(g)):
        if g[j] != 0:
            temp[g[j] - 1].append((g[j], i, j))
    graph.append(g)

S, X, Y = map(int, input().split())
virus = deque(temp)


def BFS(start):
    global graph
    global virus
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for s in start:
        k, x, y = s
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny]=k
                virus.append([(k, nx, ny)])


for s in range(S):
    if graph[X - 1][Y - 1] != 0:
        break
    for i in range(len(virus)):
        start = virus.popleft()
        BFS(start)

print(graph[X - 1][Y - 1])
