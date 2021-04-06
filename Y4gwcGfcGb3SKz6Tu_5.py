
def max_separator(s):
    res = []
    for c in set(s):
        s1 = s[:]
        while s1.count(c) > 1:
            start = s1.find(c)
            s1 = s1[start + 1:]
            len_sub = s1.find(c) + 2
            res.append((len_sub, c))
    if res:
        res.sort(key=lambda t: (-t[0], t[1]))
        max_len = res[0][0]
        return [t[1] for t in res if t[0] == max_len]
    return []

