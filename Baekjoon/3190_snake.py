n = int(input())
ground = [[0] * (n) for _ in range(n)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    ground[x - 1][y - 1] = 1

direction_list = []
for _ in range(int(input())):
    x, direction = input().split()
    direction_list.append((int(x), direction))

direction_x = [0, 1, 0, -1]
direction_y = [1, 0, -1, 0]
direction_index = 0
head = (0, 0)
body = []
time = 0
while True:
    time += 1
    nx = head[0] + direction_x[direction_index]
    ny = head[1] + direction_y[direction_index]
    if not (0 <= nx < n and 0 <= ny < n and (nx, ny) not in body):
        break

    if ground[nx][ny]:
        body.append((head[0],head[1]))
        head = ((nx, ny))
    else:
        body.append((head[0],head[1]))
        body.pop(0)
        head = ((nx, ny))

    if len(direction_list) > 0 and direction_list[0][0] == time:
        if direction_list[0][1] == "D":
            direction_index = (direction_index + 1) % 4
        else:
            direction_index = (direction_index - 1) % 4
        direction_list.pop(0)

    # print(time, (nx,ny), head,body, ground[nx][ny], direction_list)
print(time)
