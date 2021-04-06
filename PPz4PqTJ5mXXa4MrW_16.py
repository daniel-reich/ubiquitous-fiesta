
def ulam(n):
    if n in (1,2):
        return n
    m = 3
    s = [1,2]
    nexts, skips = {3}, set()
    while len(s) < n:
        while (m not in nexts) or (m in skips):
            m += 1
        for x in s:
            if x+m in nexts:
                skips.add(x+m)
            else:
                nexts.add(x+m)
        s.append(m)
        m += 1
    return s[-1]

