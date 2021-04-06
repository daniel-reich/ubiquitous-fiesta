
def find_broken_keys(txt1, txt2):
    out = []
    for x,y in enumerate(txt1):
        if y not in out and y != txt2[x]:
            out.append(y)
    return out

