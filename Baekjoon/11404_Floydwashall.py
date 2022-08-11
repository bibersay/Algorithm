import sys

N = int(input())
E = int(input())
graph = [[1e9] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for i in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    if graph[a][b] > w:
        graph[a][b] = w


def Floyd():
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])


Floyd()
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if graph[a][b] == 1e9:
            print("0", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
