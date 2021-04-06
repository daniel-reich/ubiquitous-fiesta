
def ulam(q):
​
    l = [1, 2]
    n = 3
    while len(l) < q:
        c = 0
        for i in l:
            if n - i < i and n - i in l:
                c += 1
            if c > 1:
                break
        if c == 1:
            l.append(n)
        n += 1
    return l[-1]

