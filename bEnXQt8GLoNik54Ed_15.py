
def max_score(s):
    m = 0
    for i in range(len(s)):
        l, r = s[0: i + 1], s[i + 1:]
        if len(l) >= 1 and len(r) >= 1:
            calc = len(l.replace('1', '')) + len(r.replace('0', ''))
            m = calc if calc > m else m
    return m

