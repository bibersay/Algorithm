def solution(matrix):
    answer = 0
    matrix_transpose = [[*m] for m in zip(*matrix)]
    # print(matrix)
    # print(matrix_transpose)
    for i in range(len(matrix)):
        m = sorted(matrix[i])
        target_num = m[len(matrix) // 2]
        # print(target_num)
        target_index = matrix[i].index(target_num)
        # print(f'{target_index=}, {target_num=}')

        m_t = sorted(matrix_transpose[target_index])
        # print(f'{m_t=}, {target_num=}')

        if target_num == m_t[len(matrix_transpose) // 2]:
            answer += 1

    return answer


matrix = [[1, 19, 20, 8, 25], [21, 4, 3, 17, 24], [12, 5, 6, 16, 15], [11, 18, 10, 9, 23], [7, 13, 14, 22, 2]]
print(solution(matrix))
