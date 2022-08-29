import sys


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    parent[a] = b
    return parent


N = int(input())
x_e = []
y_e = []
z_e = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    x_e.append((x, i))
    y_e.append((y, i))
    z_e.append((z, i))
x_e.sort()
y_e.sort()
z_e.sort()

edge = []

for j in range(1, N):
    cost = x_e[j][0] - x_e[j - 1][0]
    edge.append((cost, x_e[j - 1][1], x_e[j][1]))
    cost = y_e[j][0] - y_e[j - 1][0]
    edge.append((cost, y_e[j - 1][1], y_e[j][1]))
    cost = z_e[j][0] - z_e[j - 1][0]
    edge.append((cost, z_e[j - 1][1], z_e[j][1]))
edge.sort()
parent = [i for i in range(N + 1)]
result = 0
cnt = 0
for e in edge:
    c, a, b = e
    if find(a, parent) != find(b, parent):
        parent = union(a, b, parent)
        result += c
        cnt += 1
    if cnt == N - 1:
        break
print(result)
