
def less_or_equal(lst, k):
    r = [1] + sorted(lst)    
    return r[k] if len(lst) == k or r[k] != r[k + 1] else None

