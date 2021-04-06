
pt = [[1], [1,1]]
for i in range(1, 30):
    r = [1]
    for j in range(1, len(pt[i])):
        r.append(pt[i][j-1] + pt[i][j])
    pt.append(r + [1])
​
def term(c, p, m):
    t = ''
    if c > 1: t += str(c)
    if p > 0: t += 'a' + ('' if p == 1 else '^' + str(p))
    if m > 0: t += 'b' + ('' if m == 1 else '^' + str(m))
    return t
​
def Formula(n):
    if n == 0: return '1'
    positive = n > 0
    n = abs(n)
    m = len(pt[n])
    exp = '+'.join([term(c, m - p - 1, p) for p, c in enumerate(pt[n])])
    return exp if positive else '1/({})'.format(exp)

