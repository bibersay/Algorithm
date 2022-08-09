
def solution(maps):
    answer = 0
    pos = [0,0]
    n = len(maps)
    m = len(maps[0])
    visit = [[0]*m for _ in range(n)]
    cnt = 0

    def dfs(pos, cnt):
        x = pos[0]
        y = pos[1]
        if x <= -1 or m-1 < x or y<=-1 or n-1 < y or maps[x][y]==0:
            return
        elif maps[x][y]:
            if visit[x][y]:
                return
            else :
                visit[x][y] =1

        if pos == [n - 1, m - 1]:
            answer.append(cnt)
            visit[x][y]=0
            cnt -=1
            return

        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in direct:
            temp = pos
            temp[0] += d[0]
            temp[1] += d[1]
            dfs(temp, cnt + 1)

        visit[x][y]=0
        cnt-=1
        return

    dfs(pos,cnt+1)



    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))