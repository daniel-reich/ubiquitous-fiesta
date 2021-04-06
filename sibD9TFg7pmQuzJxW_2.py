
def stem_plot(lst):
    lst = ['{:0>2}'.format(str(i)) for i in lst]
    d = {}
    for i in lst:
        k,v = i[:-1],i[-1]
        if k not in d: d[k] = ''
        d[k] += v
    return ['{} | {}'.format(k,' '.join(sorted(d[k]))) for k in sorted(d.keys(),key=lambda x:int(x))]

