def solution(card, word):
    answer = []

    alphas = dict()
    r=0
    for c in card:
        r +=1
        for cc in c :
            if cc not in alphas:
                alphas[cc] = (r,1)

            else :
                alphas[cc] = (r,alphas[cc][1]+1)
    # print(alphas)

    same = set()
    same.add(1)
    same.add(2)
    same.add(3)
    for w in word:
        temp = alphas.copy()
        # print(f'{temp=}')
        # print(f'{alphas=}')
        row = set()
        # print(temp)
        for c in w:
            if c in temp:
                # print(f'{c} {temp[c]=}')
                temp[c] = (temp[c][0],temp[c][1]-1)
                row.add(temp[c][0])
                # print(f'{temp[c]=} {row=}')

                if temp[c][1] <0:
                    break
            else:
                break
        else:
            # print(f'{same=}, {row=}')
            if same == row:
                answer.append(w)
            # print(c)


    # print(card, word)
    if not answer:
        answer = ["-1"]
    return answer


card = ["AABBCCDD", "KKKKJJJJ", "MOMOMOMO"]
word = ["AAAKKKKKMMMMM", "ABCDKJ"]

card = ["ABACDEFG", "NOPQRSTU", "HIJKLKMM"]
word = ["GPQM", "GPMZ", "EFU", "MMNA"]
print(solution(card, word))
