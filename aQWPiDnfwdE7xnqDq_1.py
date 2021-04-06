
def drange(*args):
    if len(args) == 1:
        return tuple(range(args[0]))
    elif len(args) == 2:
        return tuple(range(args[0], args[1]))
    else:
        start, stop, step = args
        rnd = 0
        if any('.' in str(i) for i in [start,stop,step]):
            rnd = max(len(str(i).split('.')[-1]) for i in [start, stop, step] if i%1)
            
        lst = [start]
        while lst[-1] + step < stop:
            lst.append(round(lst[-1]+step,rnd))
        return tuple(lst)

