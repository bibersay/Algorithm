from itertools import permutations


def opertaion(temp, operand):
    stack = []
    calculate = False

    for i, symbol in enumerate(temp):
        if calculate:
            stack.pop()
            num1 = stack.pop()
            num2 = symbol
            calculate = False

            if operand == '-':
                stack.append(num1 - num2)
            if operand == '*':
                stack.append(num1 * num2)
            if operand == '+':
                stack.append(num1 + num2)
            continue
        if symbol == operand:
            calculate = True

        stack.append(symbol)

    return stack


def solution(expression):
    symbols = []
    temp = ''
    for e in expression:
        if e in '-*+':
            symbols.append(int(temp))
            symbols.append(e)
            temp = ''
        else:
            temp += e
    symbols.append(int(temp))
    orders = list(permutations('-*+', 3))
    result = []

    for order in orders:
        first, second, third = order
        temp = symbols[:]

        temp = opertaion(temp, first)
        temp = opertaion(temp, second)
        temp = opertaion(temp, third)
        result.append(abs(*temp))
    answer = max(result)
    return answer


expression = "50*6-3*2"
print(solution(expression))
