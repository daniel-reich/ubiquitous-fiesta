
def sum_missing_numbers(lst):
    m1 = min(lst)
    m2 = max(lst)
    ctr = 0
    for i in range(m1,m2+1):
        if i not in lst:
            ctr += i
    return ctr

