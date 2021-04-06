
def s(ls, func, total, i=0):
    while i+1 < total:
        if i == 0: value = func([a for a in ls if a != '0'])
        else: value = func(ls[i:])
        p = (total-1) - ls[::-1].index(value, 0,total-i)
        if p > i and ls[i] != ls[p]: ls[i], ls[p] = ls[p], ls[i]; break
        i += 1
    return ''.join(ls)
​
def maxmin(n):
    t = [i for i in str(n)]; m = t.copy(); u, d = s(m, max, len(m)), s(t, min, len(t))
    return int(u), int(d)

