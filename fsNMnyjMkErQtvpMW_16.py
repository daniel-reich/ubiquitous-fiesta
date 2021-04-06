
def holey_sort(lst):
    t_v = []
    d = {'4':1,'6':1,'8':2,'0':1,'9':1}
    lst = lst = [str(a) for a in lst]
    for a in lst:
        ls = 0
        for b in a:
            if b in d:
                ls+=d[b]
            else:
                ls+=0
        t_v.append((a,ls))
    a = lambda x:x[1]
    return [int(a[0]) for a in sorted(t_v,key=a,reverse = False)]

