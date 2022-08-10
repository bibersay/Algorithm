# set 자료형 사용
"""
N = int(input())
number_N = set(map(int,input().split()))
M = int(input())
number_M = list(map(int,input().split()))


for m in number_M:
    if m in number_N:
        print(1)
    else :
        print(0)
"""

N = int(input())
number_N = list(map(int, input().split()))
number_N.sort()
M = int(input())
number_M = list(map(int, input().split()))

print(number_N)


def binary_search_while(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return 1
        elif target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
    return 0

def binary_search_recur(arr, target, start, end):
    if start > end:
        return -1
    else :
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            return binary_search_recur(arr, target, start, mid-1)
        elif target > arr[mid]:
            return binary_search_recur(arr, target, mid+1, end)
for i in number_M:
    print(binary_search_while(number_N, i, 0, len(number_N) - 1))
    print(binary_search_recur(number_N, i, 0, len(number_N) - 1))
