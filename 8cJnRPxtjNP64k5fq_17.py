
def dance(lst,parameter):
    w = [x for x, y in lst]
    m = [y for x, y in lst]
    if parameter == 'men':
        m = m[::-1]
    else:
        w = w[::-1]
    return [[w[i], m[i]] for i in range(len(m))]

