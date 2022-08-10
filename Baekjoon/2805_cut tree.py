import sys

N, K = sys.stdin.readline().split()
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

while True:
    if start > end:
        break
    else :
        mid = (start + end )//2
        length = 0
        for tree in trees:
            if tree - mid >=0:
                length += tree - mid

        if length >= int(K):
            start = mid +1
        else :
            end = mid -1

print(end)