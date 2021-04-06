
def widen_streets(lst, n):
    res = []
    for col in zip(*lst):
        if col[-1] == ' ':
            res += [col]*n
        else:
            res += [col]
    return [''.join(i) for i in zip(*res)]

