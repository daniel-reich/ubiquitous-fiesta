
def secret_word(s, length):
    v, comp, le = [], [], len(s) - 2
    for i in enumerate(range(le)):
        v.append([sum(map(ord, s[i[0]:i[0]+3])) - 288, i[0]])
    for start in range (le-length+1):
        p = [v[start]]
        for sec in range(start+1, le-length+2):
            po, d = p + [v[sec]], v[sec][0]-p[-1][0]
            for r in range(sec+1, le):
                po += [v[r]] if v[r][0]-po[-1][0] == d else []
            if len(po) >= length:
                return "".join([s[i[1]+1] for i in po[:length]])

