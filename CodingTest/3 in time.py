def solution():
    result = 0

    for h in range(6):
        for m in range(60):
            for s in range(60):
                # if h == 3 or m == 3 or s == 3:
                #     result += 1
                # elif h % 10 == 3 or m % 10 == 3 or s % 10 == 3:
                #     result += 1
                if '3' in str(h)+str(m)+str(s):
                    result+=1
    return result


print(solution())
