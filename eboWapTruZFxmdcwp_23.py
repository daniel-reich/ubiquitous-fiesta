
def is_positive_dominant(lst):
    n = 0
    p = 0
    l = list(set(lst))
    for i in range(len(l)):
        if l[i] > 0:
            p += 1
        if l[i] < 0:
            n += 1
    return p > n

