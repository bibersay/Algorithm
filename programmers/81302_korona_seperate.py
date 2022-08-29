from collections import deque


def searh(board):
    def BFS(start):
        x, y = start
        cnt = 0
        queue = deque()
        queue.append((x, y, cnt))
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while queue:
            x, y, cnt = queue.popleft()
            board[x][y] = 'X'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] != "X":

                    if board[nx][ny] == 'P' and cnt <= 1:
                        return False
                    if cnt <= 1:
                        queue.append((nx, ny, cnt + 1))
                    board[nx][ny] = 'X'

        return True

    temp = [b[:] for b in board]
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'P':
                if not BFS((i, j)):
                    return False
                board = [t[:] for t in temp]

    return True


def solution(places):
    answer = []

    for place in places:
        board = [[i for i in p] for p in place]
        if searh(board):
            answer.append(1)
        else:
            answer.append(0)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
