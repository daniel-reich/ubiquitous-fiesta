
def priority_sort(lst, s):
    flst = sorted([i for i in lst if i not in s])
    fst = sorted([i for i in lst if i in s])
    return fst + flst

