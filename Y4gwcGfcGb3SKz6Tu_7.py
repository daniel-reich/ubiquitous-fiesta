
def max_separator(txt):
    r = []
    d = sorted([[y, x] for x, y in enumerate(txt)], key=lambda x : x[0])
    last = d[0][0]
    for i in range(1, len(d)):
        if d[i][0] == last:
            add = [d[i][1] - d[i - 1][1], d[i][0]]
            r.append(add)
        last = d[i][0]
    r = sorted(r, key=lambda x : x[0], reverse=True)
    return sorted([y for x, y in r if x == r[0][0]])

