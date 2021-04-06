
def rank(lst):
    d = {}
    for idx, i in enumerate(sorted(lst)):
        if i in d:
            d[i][0] += idx
            d[i][1] += 1
        else:
            d[i] = [idx, 1]
    return [d[i][0]/d[i][1] for i in lst]

