
def sig_figs(num):
    first = -1
    s = ''.join([x for x in num if x.isdigit()])
    last = len(s) - 1
    for i,x in enumerate(s):
        if x != '0' and first < 0 and x.isdigit():
            first = i
        if x != '0' and '.' not in num:
            last = i
    if first < 0:
        return 0
    return last - first + 1

