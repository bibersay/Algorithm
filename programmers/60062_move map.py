"""
현재위치 pos = [(x,y)(w,v)]
이동 체크 : def move_check
            def move
            pos 좌우상하 확인
            horizon 좌우 1, 상하 2 vertical 좌우 2 상하1
            현재 방향 horizen, vertical
 이동
 회전 체크 def rotation_check
 회전     def rotation

 start -> BFS
queue(start)
 while 도착까지:
    for in 4
        좌우상하 이동 체크
        이동
        회전 체크
        회전
        백트래킹

변수
grid = 지형정보
visit = 방문정보
rotation_index = vertical, horizen
cnt 이동횟수

"""

def move():
    return
def rotation():
    return
def BFS(start, i):
    return


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
def solution(board):
    answer = 0
    h = 0
    v = 1
    rotation_index = h
    cnt = 0
    answer = BFS((0,0),cnt)
    return answer

print(solution(board))


