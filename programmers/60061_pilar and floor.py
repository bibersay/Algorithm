def check(result):
    for x, y, frame in result:
        if frame == 0:
            if y == 0 or \
                    (x, y - 1, 0) in result or \
                    (x - 1, y, 1) in result or \
                    (x, y, 1) in result:
                continue
            return False
        elif frame == 1:
            if (x, y - 1, 0) in result or \
                    (x + 1, y - 1, 0) in result or \
                    ((x - 1, y, 1) in result and (x + 1, y, 1) in result):
                continue
            return False
    return True


def solution(n, build_frame):
    result = []
    for order in build_frame:
        print(order, result)
        item = (order[0], order[1], order[2])
        if order[3]:
            result.append(item)
            if not check(result):
                result.remove(item)
        else:
            result.remove(item)
            if not check(result):
                result.append(item)
    return sorted(result)


build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
               [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
n = 5
print(solution(n, build_frame))
