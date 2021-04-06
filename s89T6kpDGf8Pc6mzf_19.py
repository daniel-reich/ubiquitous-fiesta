
def seven_segment(txt):
    d = {
        '0':'abcdef', '1':'bc', '2':'abdeg', '3':'abcdg', '4':'bcfg',
        '5':'acdfg', '6':'acdefg', '7':'abc', '8':'abcdefg', '9':'abcfg'
        }
​
    res = []
    for i in range(1, len(txt)):
        sa = set(d[txt[i-1]])
        sb = set(d[txt[i]])
        off = sa - sb
        on = sb - sa
        r = []
        for v in off:
            r.append(v)
        for v in on:
            r.append(v.upper())
        r.sort(key=lambda v:v.lower())
        res.append(r)
    return res

