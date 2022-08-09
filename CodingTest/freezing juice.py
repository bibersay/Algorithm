N, M = input().split()
graph = [list(map(int, input())) for x in range(int(N))]
print(graph)
cnt = 0
def dfs(x, y):      # 전방향 모두 탐색
    global cnt
    if 0 <= x <= int(N)-1 and 0 <= y <= int(M)-1:
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
        else :
            return False
        return True
    else:
        return False
for j in range(int(N)): # 모든 지점 탐색
    for k in range(int(M)):
        if dfs(j, k) ==True:
            cnt +=1

print(cnt)
