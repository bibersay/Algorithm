def solution(rows, columns, queries):
    answer = []

    matrix = [[j * columns + (i + 1) for i in range(columns)] for j in range(rows)]
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        sum_list = []
        temp = matrix[x1][y1]
        sum_list.append(temp)
        for j in range(x2 - x1):
            matrix[x1 + j][y1] = matrix[x1 + (j + 1)][y1]
            sum_list.append(matrix[x1 + j][y1])
        for i in range(y2 - y1):
            matrix[x2][y1 + i] = matrix[x2][y1 + i+1]
            sum_list.append(matrix[x2][y1 + i])
        for j in range(x2 - x1):
            matrix[x2 - j][y2] = matrix[x2 - (j + 1)][y2]
            sum_list.append(matrix[x2 - j][y2])
        for i in range(y2 - y1):
            matrix[x1][y2 - i] = matrix[x1][y2 - (i + 1)]
            sum_list.append(matrix[x1][y2 - i])

        matrix[x1][y1+1] = temp
        answer.append(min(sum_list))

    return answer


rows = 100
columns = 97
queries = [[1,1,100,97]]
print(solution(rows, columns, queries))
