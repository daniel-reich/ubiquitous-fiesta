
def simple_check(a, b):
    lo, hi = min(a,b), max(a,b)
    cnt = 0
    for i in range(lo):
        if hi % lo == 0:
            cnt += 1
        hi = hi - 1
        lo = lo - 1
    return cnt

