
def get_quartiles(lst, method):
    lst.sort()
    q0, q4 = lst[0], lst[-1]
    q2, lo, hi = get_median(lst, method)
    if method in ('MM', 'T'):
        q1, a, b = get_median(lo, method)
        q3, a, b = get_median(hi, method)
    else:
        i = (len(lst) + 1) / 4
        q1 = lst[-1 + rnd(i, 'up')]
        q3 = lst[-1 + rnd(3*i,'down')]
    return [q0, q1, q2, q3, q4]
​
def rnd(i, dir):
    if '.5' in str(i):
        if dir == 'up':
            i = i + .1
        else:
            i = i - .1
    return round(i)                    
​
def get_median(x, meth):
    lo, hi = [], []
    idx = (len(x) - 1) // 2
    if len(x)% 2 == 0:
        med = (x[idx] + x[idx+1]) / 2
        lo = x[:idx+1]
        hi = x[idx+1:]           
    else:
        med = x[idx]
        if meth == 'T':
            lo = x[:idx+1]
            hi = x[idx:]
        if meth == 'MM':
            lo = x[:idx]
            hi = x[idx+1:]
    return med, lo, hi

