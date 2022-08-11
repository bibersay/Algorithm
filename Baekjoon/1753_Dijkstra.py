import heapq
import sys
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V +1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w,v))

dis = [1e9] * (V+1)


def Dijkstra(start):
    dis[start] = 0
    q = []
    heapq.heappush(q, (0,start))

    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for wei, node in graph[now]:
            if dist + wei < dis[node]:
                dis[node] = dist + wei
                heapq.heappush(q, (dist+wei,node))

Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dis[i] == 1e9 else dis[i])