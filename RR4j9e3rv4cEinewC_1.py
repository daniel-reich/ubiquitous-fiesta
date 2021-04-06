
def hats(lst):
    n, lines = lst
    lo = n*(min(lines))//5-1
    hi = 10*(n+100)*min(lines)+50
    while hi-lo > 1:
        h = (hi+lo)//2
        if n > sum(h // l for l in lines):
            lo = h
        else:
            hi = h
    k = sum(hi // l for l in lines)
    return "{} minute{}".format(hi, 's' if hi > 1 else '') if n == k else None

