from collections import deque

n = int(input())
graph = []
pos = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j, size in enumerate(row):
        if size != 0 and size != 9:
            pos.append((i, j, size))
        if size == 9:
            c_x, c_y = i, j


def bfs(start, targets, now_size):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    distances = []
    for t in targets:
        x, y = start
        visit = [[0] * (n) for _ in range(n)]
        visit[x][y] = 1
        stop_target = False

        t_x, t_y, target_size = t
        if target_size >= now_size:
            break
        cnt = 0
        queue.append((x, y, cnt))
        while queue:
            if stop_target:
                break
            x, y, cnt = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and graph[nx][ny] <= now_size:
                    if t_x == nx and t_y == ny:
                        distances.append((cnt + 1, nx, ny, t))
                        stop_target = True
                        break
                    visit[nx][ny] = 1
                    queue.append((nx, ny, cnt + 1))
        print(t, distances)
    if len(distances) == 0:
        return (-1, x, y, targets[0])
    distances.sort()
    pos.pop(pos.index(distances[0][3]))
    return distances[0]


target_size = 1
now_size = 2
time = 0
ate = 0
if pos:
    pos.sort(key=lambda x: (x[2], x[0], x[1]))
    stop = False
    while pos:
        if pos[0][2] >= now_size:
            break
        if stop == True:
            break
        dis, c_x, c_y, _ = bfs((c_x, c_y), pos, now_size)
        if dis == -1:
            stop = True
            break
        time += dis
        print(c_x, c_y,'time',time, dis)
        ate += 1
        if ate >= now_size:
            ate = 0
            now_size += 1

print(time)
