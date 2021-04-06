
def min_length(lst, n):
    m = len(lst) + 1
    for i in range(1, len(lst) + 1):
        for j in range(len(lst)):   
            check = lst[j : j + i]
            if sum(check) > n:
                m = min(m, len(check))
    if m == len(lst) + 1:
        m = - 1
    return m

