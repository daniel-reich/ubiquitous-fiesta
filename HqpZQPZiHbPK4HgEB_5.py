
def exchange(n, i, j):
    nl = list(n)
    nl[i], nl[j] = nl[j], nl[i]
    return ''.join(nl)
​
def maxmin(num):
    n = m = str(num)
    for i, ch in enumerate(n[:-1]):
        if ch < max(n[i+1:]):
            j = n.rindex(max(n[i+1:]))
            n = exchange(n, i, j)
            break
    if num > 9:
        minch = min(m[1:], key=lambda c: '9' if c=='0' else c)
        if m[0] > minch:
            j = m.rindex(minch)
            m = exchange(m, 0, j)
        else:
            for i, ch in enumerate(m[1:-1], 1):
                if ch > min(m[i+1:]):
                    j = m.rindex(min(m[i+1:]))
                    m = exchange(m, i, j)
                    break
​
    return int(n), int(m)

