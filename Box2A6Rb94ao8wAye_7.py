
def leader(lst):
    x = lst[lst.index(max(lst)):]
    if x==sorted(x, reverse=True):
        return x
    return [x[i+1] if x[i+1]>x[i] else x[i] for i in range(len(x)-1)]

