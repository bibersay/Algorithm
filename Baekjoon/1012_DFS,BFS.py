from collections import deque
import sys
sys.setrecursionlimit(10000)
def BFS(x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y]=0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    # print(x,y)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny]=0
                    # queue.append((nx, ny))
                    BFS(nx,ny)

def DFS(x,y):
    stack = deque()
    graph[x][y] = 0
    stack.append((x,y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0<=ny < n:
                if graph[nx][ny] == 1:
                    DFS(nx,ny)

N = int(input())
for _ in range(N):
    cnt = 0
    m, n, K = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    # queue = deque()
    # queue.append((0,0))
    for k in range(m):
        for j in range(n):
            if graph[k][j]:
                BFS(k, j)
                cnt +=1
    print(cnt)