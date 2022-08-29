import copy
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
temp = [[0] * M for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))


def BFS(start, temp, result):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([start])
    temp[start[0]][start[1]] = 8
    result = 1
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                queue.append((nx, ny))
                temp[nx][ny] = 8
                result += 1

    return result


comb = []
wall = 0
virus = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 0:
            comb.append((i, j))
        elif graph[i][j] == 1:
            wall += 1
        elif graph[i][j] == 2:
            virus.append((i,j))
combinations = list(combinations(comb, 3))

result = N * M + 1
for c in combinations:
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            temp[i][j] = graph[i][j]

    # temp = copy.deepcopy(graph)
    for x, y in c:
        temp[x][y] = 5

    cnt = 0
    for x,y in virus:
        cnt += BFS((x, y), temp, cnt)

    result = min(cnt, result)
answer = N * M - result - wall - 3
print(answer)
