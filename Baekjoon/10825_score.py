import sys

N = int(input())
name = []
for _ in range(N):
    n, L, E, M = sys.stdin.readline().split()
    L, E, M = map(int, [L, E, M])
    name.append((n, L, E, M))
name.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(name[i][0])
