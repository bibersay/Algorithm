def solution(dirs):
    dir = ['U', "R", "D", "L"]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    directions = {}
    for i, d in enumerate(dir):
        directions[d] = (dx[i], dy[i])

    x, y = 5, 5
    trace = set()

    for d in dirs:
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            pos = [(nx,ny),(x,y)]
            pos.sort()
            X,Y = pos
            trace.add((X,Y))
            x = nx
            y = ny
    answer = len(trace)

    return answer


dirs = "LRDU"
print(solution(dirs))
