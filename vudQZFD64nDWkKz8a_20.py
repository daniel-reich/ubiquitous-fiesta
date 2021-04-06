
def grant_the_hint(s):
    s = s.split()
    m = len(max(s, key=len))
    h = [[] for _ in range(m+1)]
    for x in range(m + 1):
        for w in s:
            h[x].append(''.join([w[:x]] + ['_' for _ in w[x:]]))
    return [' '.join(w) for w in h]

