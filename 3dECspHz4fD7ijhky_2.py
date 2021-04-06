
def numbers_range(r):
    if not r:
        return ''
    elif len(r) == 1:
        return str(r[0])
    s, e, res = 0, 0, ''
    for i in range(1, len(r)):
        if r[i] - r[i - 1] == 1 and i < len(r) - 1:
            e = i
        else:
            if i == len(r) - 1:
                e = i
            if s == e:
                res += '{}, '.format(str(r[s]))
            elif e - s == 1:
                res += '{}, {}, '.format(str(r[s]), str(r[e]))
            else:
                res += '{}-{}, '.format(str(r[s]), str(r[e]))
            s = i
            e = i
    return res[: -2]

