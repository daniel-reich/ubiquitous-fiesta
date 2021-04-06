
def is_valid(s):
    r = []
    l = []
    d = []
    for i in s:
        if i not in l:
            l.append(i)
            if s.count(i) not in r:
                r.append(s.count(i))
            d.append(s.count(i))
    if len(r) == 1:
        return "YES"
    elif len(r) > 2:
        return "NO"
    else:
        d.sort()
        if d[0] == d[1] and d[len(d) - 1] == d[len(d) - 2]:
            print('r')
            return "NO"
        else:
            if d[0] + 1 == d[len(d) - 1]:
                return "YES"
            else:
                return "NO"

