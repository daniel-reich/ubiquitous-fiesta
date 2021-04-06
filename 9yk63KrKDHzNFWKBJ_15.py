
def is_it_inside(fd, x, y):
    if y not in fd or x == y: return x == y
    f, s, p = y, [], [y]
    while f:
        if x in fd[f]: return True
        for n in fd[f]:
            if n in fd and n not in s:
                s, p, f = s+[n], p+[n], n; break
            p.pop()
            if not p: return False
            f = p[-1]

