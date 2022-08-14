def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2 +1):
        cnt = 1
        compress = ''
        for j in range(0,len(s),i):
            if s[j:j+i] == s[j+i:j+2*i]:
                cnt +=1
            else:
                if cnt == 1:
                    compress +=s[j:j+i]
                    cnt = 1
                elif cnt>1:
                    compress += str(cnt) + s[j:j+i]
                    cnt = 1
        answer.append(len(compress))
    answer = min(answer)
    return answer

s = "aabbaccc"
print(solution(s))

def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, int(len(s) /2) + 1):
        cnt = 1
        ans = ''
        for j in range(0, len(s), i):
            if s[j : j+i] == s[j+i : j+ i*2]:
                cnt +=1
            elif cnt >=2:
                ans += str(cnt) + s[j:j+i]
                cnt = 1
            else :
                ans += s[j : j+i]
        answer.append(ans)
    # print(answer)
    answer = min(map(len,answer))
    # print(answer)
    return answer
