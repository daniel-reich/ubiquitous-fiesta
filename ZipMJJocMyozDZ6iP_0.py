
def group(lst, size):
    from math import ceil
    d = ceil(len(lst)/size)
    return [[lst[ii] for ii in range(i,len(lst),d)] for i in range(d)]

