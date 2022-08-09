def solution():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    pos = [1, 1]
    N = 3

    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3

    cnt = 1
    turn_time = 0
    arr = [[]]

    while True:
        turn_left()
        turn_time += 1
        if turn_time == 4:
            pos[0] -= dx[direction]
            pos[1] -= dy[direction]
            turn_time = 0

            continue

        if 0 <= pos[0] + dx[direction] <= N and 0 <= pos[1] + dy[direction] <= N \
                and arr[pos[0]][pos[1]] != 1:
            pos[0] += dx[direction]
            pos[1] += dy[direction]
            arr[pos[0]][pos[1]] = 1
            cnt += 1

        else:
            continue

    return


print(solution())
