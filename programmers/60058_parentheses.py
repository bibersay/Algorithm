def index(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            cnt -= 1

        if cnt == 0:
            return i


def check(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer

    pos = index(p)
    print(pos)
    u = p[:pos + 1]
    v = p[pos + 1:]
    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer = ''.join(u)
    return answer


p = "))(("
print(solution(p))
