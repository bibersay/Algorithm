graph = [[0] * 4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        graph[i][j] = (data[j * 2], data[j * 2 + 1])

result = graph[0][0][0]
direction = graph[0][0][1]
shark = (0, 0, direction)
graph[0][0] = (0, 0)


def find_fish(graph, num):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return i, j, graph[i][j][1]

    return (-1, -1, -1)


def move_fish(graph, shark):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    s_x, s_y, _ = shark
    for i in range(1, 17):
        x, y, d = find_fish(graph, i)
        if x == -1:
            continue
        for j in range(len(dx)):
            d = (d + j - 1) % 8
            nx = x + dx[d]
            ny = y + dy[d]

            # print(f'{x=},{y=},{d=}, {nx=},{ny=}')
            if 0 <= nx < 4 and 0 <= ny < 4 and \
                    (nx,ny) != (s_x,s_y):
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                break
    return graph


def find_move_shark(graph, shark):
    candidates = []
    nx, ny, direction = shark
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    for i in range(4):
        nx = nx + dx[direction - 1]
        ny = ny + dy[direction - 1]
        if 0 <= nx < 4 and 0 <= ny < 4 and \
                graph[nx][ny][0] != 0:
            candidates.append((nx, ny, graph[nx][ny][0], graph[nx][ny][1]))

    return candidates


def BFS(shark, graph, result):
    graph = move_fish(graph, shark)

    candidates = find_move_shark(graph, shark)

    if len(candidates) == 0:
        return result
    candidate_result = []
    for candidate in candidates:
        nx, ny, fish_num, fish_direction = candidate
        shark = (nx, ny, fish_direction)

        graph[nx][ny] = (0, 0)
        print(f'{result=} {fish_num=}')
        candidate_result.append(BFS(shark, graph, result + fish_num))

        graph[nx][ny] = (fish_num, fish_direction)

    return max(candidate_result)


print(BFS(shark, graph, result))
