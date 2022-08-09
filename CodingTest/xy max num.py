def solution(X, Y):
    answer = ''

    temp_x = [0] * 10
    temp_y = [0] * 10
    temp = [0] * 10
    if len(X) ==0 or len(Y) ==0:
        return '0'

    for x in X :
        temp_x[int(x)] +=1

    for y in Y :
        temp_y[int(y)] +=1

    for i in range(10):
        if temp_x[i] * temp_y[i]:
            temp[i] = max(temp_x[i], temp_y[i])
            answer += str(str(i) * temp[i])
        if i == 0 and temp[i] !=0:
            answer += '0'


    if answer =='':
        return '-1'
    answer = answer[::-1]


    return answer


x = '100'
y = '2345'

print(solution(x, y))
