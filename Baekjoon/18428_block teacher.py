"""
n^2 = 최대 36 combination 3개 : 5천개/ combination 또는 DFS
T의 상하좌우와 S 사이에 O가 있는지 완전탐색 : check 함수

변수
graph = X : 빈칸
        S : 학생
        T : 선생
        O : 장애물
visit = DFS 탐색용
"""


def check():
    global graph
    global teacher
    for t in teacher:
        x, y = t
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == "S":
                        return False
                    if graph[nx][ny] == 'O':
                        break
                else:
                    break
                nx = nx + dx[i]
                ny = ny + dy[i]
    return True


def DFS(start, i):
    global stop
    if i == 3:
        if check():
            print('YES')
            stop = True
        return

    for i in range(len(graph)):
        for j in range(len(graph)):
            nx, ny = i,j
            if graph[nx][ny] == 'X':
                graph[nx][ny] = 'O'
                DFS((nx, ny), i + 1)
                if stop:
                    return
                graph[nx][ny] = 'X'

    return


N = int(input())
graph = [list(input().split()) for _ in range(N)]
visit = [[0 if graph[j][i] == 'X' else 1 for i in range(N)] for j in range(N)]
stop = False
teacher = [(i, j) for j in range(len(graph)) for i in range(len(graph)) if graph[i][j] == 'T']

DFS((0, 0), 0)

if stop == False:
    print('NO')
