
def missing_alphabets(txt):
    r, m = [], 0
    alpha = "abcdefghijklmnopqrstuvwxyz"
    dic = dict.fromkeys(alpha, 0)
    for i in alpha:
        current = txt.count(i)
        m = max(m, current)
        dic[i] = current
    for j in dic.items():
        if j[1] < m:
            add = (m - j[1]) * j[0]
            r.append(add)
    return "".join(sorted(r))

