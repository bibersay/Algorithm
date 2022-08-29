from collections import deque


def solution(priorities, location):
    answer = 0
    print_list = []
    for i, priority in enumerate(priorities):
        if i == location:
            print_list.append((priority, 1))
            continue
        print_list.append((priority, 0))
    queue = deque(print_list)
    max_value = max(priorities)

    while queue:
        now = queue.popleft()
        if now[0] >= max_value:
            answer += 1
            if now[1] == 1:
                return answer
            max_value = max(queue)[0]
        else:
            queue.append(now)



priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
