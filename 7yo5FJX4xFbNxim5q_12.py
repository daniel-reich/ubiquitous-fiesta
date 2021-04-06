
def harry(po):
    if len(po[0]) == 0:
        return -1
    a = list(map(list,zip(*po)))
    ans_1 = sum(po[len(po)-1][1:]) + sum(a[0])
    ans_2 = sum(po[0][:-1]) + sum(a[-1])
    return max(ans_1,ans_2)

