
def num_after_point(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1
​
def drange(*args):
    if (len(args)) == 1:
        return tuple(a for a in range(args[0]))
    elif (len(args)) == 2:
        return tuple(a for a in range(args[0], args[1]))
    else:
        start, end, step = args
        decimal = max(list(map(num_after_point, args)))
        res = []
​
        while True:
            if start >= end:
                break
            res.append(round(start, decimal))
            start += step
        
        return tuple(res)

