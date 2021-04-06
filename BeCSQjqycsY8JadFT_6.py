
def recur_index(txt, d=None, cur=0):
    if txt == None or len(txt) == 0:
        return {}
    if d == None:
        d = {txt[0]: cur}
        return recur_index(txt[1:], d, cur + 1)
    c = txt[0]
    if c in d:
        return {c: [d[c], cur]}
    d[c] = cur
    return recur_index(txt[1:], d, cur + 1)

