def solution(fees, records):
    answer = []
    table = {}
    base_time, base_fee, unit_time, unit_fee = fees

    for record in records:
        time, number, action = record.split()
        hh, mm = time.split(":")
        time = int(hh) * 60 + int(mm)

        if action == "IN":
            if number not in table:
                table[number] = (time, 1439, 0)
            else:
                table[number] = (time, 1439, table[number][2])
        else:
            start = table[number][0]
            last = time
            used_time = last - start
            table[number] = (last, last, used_time + table[number][2])

    for key, value in table.items():
        start = value[0]
        last = value[1]
        used_time = last - start + value[2]

        if used_time == 0:
            continue
        elif used_time <= base_time:
            cost = base_fee
        else:
            cost = base_fee + abs(-(used_time - base_time) // unit_time) * unit_fee
        answer.append((key, cost))
    answer.sort()

    return [a[1] for a in answer]


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
