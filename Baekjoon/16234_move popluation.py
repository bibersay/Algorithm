"""
BFS 탐색
1. 매일 전체 탐색 visit 0
2. 상하좌우 탐색시 인구 조건 :visit = 1, (x,y) + L <(nx,ny) < (x,y) + R
3. 인구 계산 : 조건 맞을시 list 추가후 sum / length
4. 인구 계산후 cnt +=1
5. 조건 없을시 종료

변수
graph 전체 인구수
sum_list 국경이 열리는 인구 추가
cnt 계산 횟수
visit 조건 확인 여부
"""
from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
sum_list = []


def BFS(start):
    x, y = start
    if visit[x][y]:
        return
    visit[x][y] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y = start
    sum_list = deque()
    queue = deque()
    queue.append((x, y))
    s = graph[x][y]
    sum_list.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
                    s += graph[nx][ny]
                    sum_list.append((nx, ny))
            else:
                continue
    if len(sum_list) >= 2:
        s = s // len(sum_list)
        for x, y in sum_list:
            graph[x][y] = s
        return True
    else:
        return False


cnt = 0
while True:
    visit = [[0] * N for _ in range(N)]
    stop = True
    for i in range(N):
        for j in range(N):
            if BFS((i, j)):
                stop = False
    if stop == True:
        break
    cnt += 1
print(cnt)
