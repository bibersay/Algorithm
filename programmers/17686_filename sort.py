import re
def solution(files):
    answer = []
    temp = []
    for order, file in enumerate(files):
        num = ''
        head = ''
        pos = len(file)-1
        print(file)
        head, tail = re.split('\d+',file.lower())
        num = (re.findall('\d+',file)[0])
        sentance= re.match(r'([a-zA-Z-.]+)(\d{,5})(.*)',file)
        print(head,num,tail, sentance)
        for i, c in enumerate(file):

            if c.isdigit():
                num+=c
            elif not c.isdigit() and num=='':
                head +=c
            elif not c.isdigit() and len(head):
                pos = i
                break

        temp.append((order, head.lower(), num.zfill(5), file[pos:]))
    temp.sort(key=lambda x: (x[1], x[2], x[0]))
    for m, n in enumerate(temp):
        answer.append(files[n[0]])

    return answer


files = ["F-5555 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))
