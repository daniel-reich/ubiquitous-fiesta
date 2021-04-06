
def super_reduced_string(txt):
    p = 0
    while len(txt) != p:
        p, i = len(txt), 1
        while i < len(txt):
            if txt[i] == txt[i-1]:
                txt = txt[:i-1] + txt[i+1:]
            else:
                i += 1
    return txt or "Empty String"

