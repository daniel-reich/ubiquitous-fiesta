
def complete_pattern(s):
    a = []
    if len(s) == 2:
        return s[0] if s[0] != '_' else s[1]
    for x in range(2,len(s)//2+1):
        a.append([s[i:i+x] for i in range(0,len(s),x) if len(s[i:i+x]) == x])
    for z in a:
        for x, y in zip(z, z[1:]):
            if '_' in x:
                c = list(x)
                c[x.index('_')] = y[x.index('_')]
                if z.count(''.join(c)) == len(z) -1 :
                    return y[x.index('_')]
            elif '_' in y:
                c = list(y)
                c[y.index('_')] = x[y.index('_')]
                if z.count(''.join(c)) == len(z) -1 :
                    return x[y.index('_')]
    for x in a:
        if len(x) == 2 and x[0] == x[1]:
            return x[0][s.index('_') % len(x[0])]

