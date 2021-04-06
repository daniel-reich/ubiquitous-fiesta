
def recur_index(txt, l = ""):
    if not txt:
        return {}
    elif txt[0] in l:
        return {txt[0] : [l.index(txt[0]), len(l)]}
    else:
        return recur_index(txt[1 : ], l + txt[0])

