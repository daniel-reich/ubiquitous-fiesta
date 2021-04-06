
def left_side(l):
    res = [0]
    for i, k in enumerate(l[1:]):
        i += 1
        count = 0
        for j in l[:i]:
            if j < k:
                count += 1
        res.append(count)
    return res
def right_side(l):
    res = []
    for i, k in enumerate(l[:-1]):
        count = 0
        for j in l[i:]:
            if j < k:
                count += 1
        res.append(count)
    res.append(0)
    return res

