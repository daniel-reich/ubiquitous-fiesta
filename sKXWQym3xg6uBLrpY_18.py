
def iqr(lst):
    lst = sorted(lst)
    beg, end, med = get_median(lst)
    b, e, q3 = get_median(end)
    b, e, q1 = get_median(beg)
    return q3 - q1
    
​
def get_median(lst):
    idx = len(lst) // 2
    if len(lst) % 2 == 1:
        m =lst[idx]
        return lst[:idx], lst[idx+1:], m
    else:
        m = (lst[idx-1] + lst[idx]) / 2
        return lst[:idx], lst[idx:], m

