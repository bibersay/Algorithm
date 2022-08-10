import sys

## 이진탐색으로 풀이
N = int(sys.stdin.readline())
numbers_N = list(map(int, sys.stdin.readline().split()))
numbers_N.sort()

M = int(sys.stdin.readline())
numbers_M = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, target, start, end):
    global cnt
    if start > end:
        return -1
    else:
        mid = (start + end) // 2
        if target == arr[mid]:
            cnt += 1
            temp = mid - 1
            while 0 <= temp and arr[temp] == target:
                cnt += 1
                temp -= 1
            temp = mid + 1
            while temp <= len(numbers_N) - 1 and arr[temp] == target:
                cnt += 1
                temp += 1
            return
        elif target <= arr[mid]:

            return binary_search(arr, target, start, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, end)


def binary_search_while(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


## dict로 풀이
numbers_N_dict = dict()
for x in numbers_N:
    if x in numbers_N_dict:
        numbers_N_dict[x] += 1
    else:
        numbers_N_dict[x] = 1

# print(' '.join(str(numbers_N_dict[m])) if m in numbers_N_dict else '0' for m in numbers_M)
for m in numbers_M:
    if m in numbers_N_dict:
        print(str(numbers_N_dict[m]), end=' ')
    else:
        print('0', end=' ')
    # binary_search(numbers_N, m, 0, len(numbers_N) - 1)
    # print(cnt, end=' ')
