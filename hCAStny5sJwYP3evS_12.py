
def is_early_bird(_range, n):
    s = []
    start = 0
    r = "".join([str(x) for x in range(_range + 1)])
    while r.find(str(n), start) != -1: 
        i = r.find(str(n), start)
        add = []
        for y in range(len(str(n))):
            add += [i + y]
        s.append(add)
        start = s[-1][1]
    if len(s) != 1:
        s += ["Early Bird!"]
    return s

