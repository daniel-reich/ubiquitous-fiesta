
def playfair(txt, keyword):
    
    shift = -1 if txt.isupper() else 1
    keyword = ''.join(sorted(set(keyword), key=lambda x: keyword.index(x)))
    txt = ''.join(i for i in txt.lower().replace('j', 'i') if i.isalpha())
    poly = keyword + ''.join(i for i in 'abcdefghiklmnopqrstuvwxyz' if i not in keyword)
    d_in = dict(zip(((i, j) for i in range(5) for j in range(5)), poly))
    d_out = {v: k for k, v in d_in.items()}
​
    res = ''
    while txt:
        if len(txt) == 1 or txt[0] == txt[1]:
            a, b = txt[0], 'x'
            txt = txt[1:]
        else:
            a, b = txt[0], txt[1]
            txt = txt[2:]
​
        (r1, c1), (r2, c2) = d_out[a], d_out[b]
        
        if r1 == r2:
            res += d_in[(r1, (c1 + shift)%5)]
            res += d_in[(r2, (c2 + shift)%5)]
        elif c1 == c2:
            res += d_in[((r1 + shift)%5, c1)]
            res += d_in[((r2 + shift)%5, c2)]
        else:
            res += d_in[(r1, c2)]
            res += d_in[(r2, c1)]
​
    return res.upper()

