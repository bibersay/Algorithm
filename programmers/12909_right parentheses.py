def solution(s):
    cnt = 0
    for i in range(len(s)):
        if s[i]=='(':
            cnt +=1
        else :
            cnt -=1
            if cnt <0:
                return False
    if cnt == 0:
        return True

    return False
s = "(()()()"
print(solution(s))