
def bifid(s):
    l = "abcdefghiklmnopqrstuvwxyz"
    c, r, out = [], [], ""
    if s[0].isupper():
        pt = "".join([i.lower() for i in s if i.isalpha()])
        for i in pt:
            pos = l.index(i)
            c.append(pos % 5)
            r.append(pos // 5)
        rc = r + c
        for i in range(1, len(rc), 2):
            out += l[rc[i - 1] * 5 + rc[i]]
    elif s[0].islower():
        for i in s:
            pos = l.index(i)
            c.append(pos // 5)
            c.append(pos % 5)
        for i in range(0, int(len(c) / 2), 1):
            out += l[c[i] * 5 + c[i + int(len(c) / 2)]]
​
    return out

