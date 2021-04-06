
from math import ceil
def c_cipher(msg, keyword):
    kwl = len(keyword)
    skw = sorted(keyword)
    if ' ' in msg:
        #encode
        sm = ''.join([c.lower() for c in msg if c.isalnum()])
        nc = ceil(len(sm)/kwl)
        rows = [sm[i:i+kwl].ljust(kwl,'x') for i in range(0,len(sm),kwl)]
        res, nr = '', len(rows)
        for k in skw:
            i = keyword.index(k)
            res += ''.join(rows[r][i] for r in range(nr))
        return res
    else:
        #decode
        nr = ceil(len(msg)/kwl)
        cols = ['']*kwl
        for i, col in enumerate([msg[i:i+nr] for i in range(0,len(msg),nr)]):
            cols[keyword.index(skw[i])] = col
        res = ''
        for i in range(nr):
            res += ''.join(col[i] for col in cols)
        return res

