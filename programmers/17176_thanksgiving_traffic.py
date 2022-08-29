def throughput(times, start, end):
    cnt = 0
    for time in times:
        if time[0] < end and time[1] >= start:
            cnt += 1
    return cnt


def solution(lines):
    answer = 0
    times = []
    for l in lines:
        day, end, duration = l.split()

        h, m, s = end.split(':')

        h = int(h) * 3600
        m = int(m) * 60
        s = float(s)
        end = (h + m + s) * 1000
        start = end - float(duration[:-1]) * 1000 + 1

        times.append((start, end))

    for time in times:
        answer = max(answer, throughput(times, time[0], time[0] + 1000), \
                     throughput(times, time[1], time[1] + 1000))

    return answer


lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]
print(solution(lines))
