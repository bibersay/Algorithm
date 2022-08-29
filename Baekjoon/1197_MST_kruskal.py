import heapq
import sys


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
edge = []

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    heapq.heappush(edge, (w, u, v))

parent = [i for i in range(V + 1)]
cost = 0

for j in range(E):
    w, u, v = heapq.heappop(edge)
    if find(u, parent) != find(v, parent):
        union(u, v, parent)
        cost += w

print(cost)
