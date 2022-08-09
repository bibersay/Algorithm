def solution(board, moves):
    answer = 0
    temp = []
    for move in moves:
        for i in board:
            if i[move-1] :
                if len(temp):
                    if temp[-1] == i[move-1]:
                        temp.pop()
                        answer +=2
                        i[move - 1] = 0
                    else :
                        temp.append(i[move-1])
                        i[move - 1] = 0
                else :
                    temp.append(i[move-1])
                    i[move - 1] = 0
                break



    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves =[1,5,3,5,1,2,1,4]

print(solution(board, moves))