def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j]:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
    answer = max(map(max,board))

    return answer**2


board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
print(solution([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]))
