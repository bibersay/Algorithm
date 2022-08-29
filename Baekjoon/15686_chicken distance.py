from itertools import combinations

n, m = map(int, input().split())
home = []
chicken = []
for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(len(graph)):
        if graph[j] == 1:
            home.append((i + 1, j + 1))
        elif graph[j] == 2:
            chicken.append((i + 1, j + 1))

candidates = list(combinations(chicken, m))
distance = 1e9
for candidate in candidates:
    length = 0
    for h in home:
        l = 1e9
        for c in candidate:
            l = min( l, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        length+=l
    distance= min(distance, length)


print(distance)
