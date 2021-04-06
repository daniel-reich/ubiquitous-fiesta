
def rank(lst):
    sorted_lst = sorted(lst)
    result = []
    for i in range(len(lst)):
        cnt = lst.count(lst[i])
        if cnt == 1:
            result.append(sorted_lst.index(lst[i]) /1)
        else:
            rank = 0
            cnt_1 = 0
            while cnt_1 < cnt:
                rank += sorted_lst.index(lst[i]) + cnt_1
                cnt_1 += 1
            result.append(rank/ cnt)
    return result

