import math
def solution(progresses, speeds):
    answer = []
    if not progresses:
        return answer
    time = math.ceil((100-progresses[0])//speeds[0])
    temp = 0
    for i,p in enumerate(progresses):
        # print(time,temp, p, speeds[i], math.ceil((100-p)//speeds[i]))
        if math.ceil((100-p)//speeds[i]) <= time:
            temp +=1
        else:
            answer.append(temp)
            temp = 1
        time = max(time,math.ceil((100-p)//speeds[i]))
    else:
        answer.append(temp)
    return answer


progresses = [2]
speeds = [1]
print(solution(progresses, speeds))