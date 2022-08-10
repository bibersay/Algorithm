import sys

K, N = map(int, sys.stdin.readline().split())

wire = list(map(int, sys.stdin.readlines()))

start = 1
end = max(wire)
max = 0
while True:
    if start > end:
        break
    mid = (start + end) // 2
    line = 0
    for i in range(K):
        line += wire[i] // mid
    if line >= N:
        if max < mid:
            max = mid
        start = mid + 1
    else:
        end = mid - 1

print(end)
