from collections import deque


def solution(board, c):
    answer = 0
    n = len(board)
    m = len(board[0])
    grid = [[1e9 for _ in range(m)] for _ in range(n)]
    # print(grid)
    for i, b in enumerate(board):
        for j, bb in enumerate(b):
            if bb == 2:
                x, y = i, j
            if bb == 3:
                ex, ey = i, j

    # print(x, y, ex, ey)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    queue = deque([(x, y)])
    grid[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                temp = grid[nx][ny]
                if board[nx][ny] == 1:
                    cost = 1 + c
                else:
                    cost = 1

                # try:
                #     grid[nx][ny] = min(grid[nx - 1][ny], grid[nx][ny], grid[x][y]) + cost
                # except:
                #     pass
                # try:
                #     grid[nx][ny] = min(grid[nx + 1][ny], grid[nx][ny], grid[x][y]) + cost
                # except:
                #     pass
                # try:
                #     grid[nx][ny] = min(grid[nx][ny - 1], grid[nx][ny], grid[x][y]) + cost
                # except:
                #     pass
                # try:
                #     grid[nx][ny] = min(grid[nx][ny + 1], grid[nx][ny], grid[x][y]) + cost
                # except:
                #     pass

                # board[nx][ny] = -1
                if grid[x][y] + cost < temp:
                    grid[nx][ny] = grid[x][y] + cost
                    queue.append((nx, ny))
                # print(f'{nx=} {ny=} {x=} {y=} {grid[nx][ny]=}')

    answer = grid[ex][ey]

    return answer


board = [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 3, 0, 0, 0, 1, 0]]
c = 2
print(solution(board, c))
