from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
# plus, minus, mul, div = map(int, input().split())
#
# operator = [1] * plus
# operator += [2] * minus
# operator += [3] * mul
# operator += [4] * div
oper = list(map(int, input().split()))
oper_len = sum(oper)
print(oper)

num_max = -1e9
num_min = 1e9 - 1


def DFS(i, num):
    global oper
    global num_max
    global num_min
    if i == oper_len:
        num_max = max(num_max, num)
        num_min = min(num_min, num)
        return

    if 0 < oper[0]:
        oper[0] -= 1
        DFS(i + 1, num + numbers[i + 1])
        oper[0] += 1
    if 0 < oper[1]:
        oper[1] -= 1
        DFS(i + 1, num - numbers[i + 1])
        oper[1] += 1
    if 0 < oper[2]:
        oper[2] -= 1
        DFS(i + 1, num * numbers[i + 1])
        oper[2] += 1
    if 0 < oper[3]:
        oper[3] -= 1
        temp = num
        if num < 0:
            num = -num
            num //= numbers[i + 1]
            num = -num
        else:
            num //= numbers[i + 1]
        DFS(i + 1, num)
        oper[3] += 1
        num = temp


DFS(0, numbers[0])

print(num_max)
print(num_min)
