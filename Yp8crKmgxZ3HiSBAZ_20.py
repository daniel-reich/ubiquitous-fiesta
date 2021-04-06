
def freq_count_rec(lst, el, depth=0, fdir=None):
    if fdir is None:
        fdir = dict()
    if not depth in fdir:
        fdir[depth] = 0
    for item in lst:
        if item == el:
            fdir[depth] += 1
        elif type(item) is list:
            freq_count_rec(item, el, depth+1, fdir)
    return fdir
​
​
def freq_count(lst, el):
    res_list = [[k, v] for k, v in freq_count_rec(lst, el).items()]
    return res_list

