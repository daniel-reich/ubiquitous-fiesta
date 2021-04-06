
def big_sub(lst):
    curr = [0, 0, -1]
    rec = [0, None, None]
    for i in range(len(lst)):
        if curr[0] <= 0:
            curr = [lst[i], i, i]
        else:
            curr[0] += lst[i]
            curr[2] += 1
        if curr[0] >= rec[0]:
            rec = curr[:]
    return rec

